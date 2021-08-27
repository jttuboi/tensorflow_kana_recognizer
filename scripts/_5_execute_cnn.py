from consts import *
import numpy as np
from numpy import mean
from numpy import std
import tensorflow as tf
import skimage.transform
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


def load_npz(kana):
    npz = np.load(kana + ".npz")['arr_0']
    array = npz.reshape([-1, FINAL_SQUARE_SIZE_Y, FINAL_SQUARE_SIZE_X]).astype(np.float32)
    array = array / np.max(array)

    #print("@A %d %d %d %d"%(len(npz), len(npz[0]), len(npz[0][0]), len(npz[0][0][0])))
    #print("@B %d %d %d"%(len(array), len(array[0]), len(array[0][0])))
    #print(array)

    kanas_quantity = len(npz)
    samples_quantity = len(npz[0])
    x_df = np.zeros([kanas_quantity * samples_quantity, TRAIN_SQUARE_SIZE_X, TRAIN_SQUARE_SIZE_Y], dtype=np.float32)
    y_df = np.repeat(np.arange(kanas_quantity), samples_quantity)

    #print("@C %d %d"%(kanas_quantity, samples_quantity))
    #print(x_df)
    #print(y_df)

    show_images_sample(array, y_df)

    for i in range(kanas_quantity * samples_quantity):
        x_df[i] = skimage.transform.resize(array[i], (TRAIN_SQUARE_SIZE_X, TRAIN_SQUARE_SIZE_Y))

    return x_df, y_df, kanas_quantity


def show_images_sample(array, y_df):
    QUANTITY_TO_SHOW = 49
    ROW = COLUMN = 7
    plt.figure(figsize=(6, 6))
    for i in range(QUANTITY_TO_SHOW):
        plt.subplot(ROW, COLUMN, i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(array[-i], cmap=plt.cm.binary)
        plt.xlabel(y_df[-i])
    plt.show()


def define_model(kanas_quantity):
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(TRAIN_SQUARE_SIZE_X, TRAIN_SQUARE_SIZE_Y, 1)))
    model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(tf.keras.layers.MaxPooling2D((2, 2)))
    model.add(tf.keras.layers.Conv2D(96, (3, 3), activation='relu'))
    model.add(tf.keras.layers.Conv2D(128, (3, 3), activation='relu'))
    model.add(tf.keras.layers.MaxPooling2D((2, 2)))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(512, activation='relu'))
    model.add(tf.keras.layers.Dense(512, activation='relu'))
    model.add(tf.keras.layers.Dense(kanas_quantity))
    model.summary()
    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])
    return model


def plot_image(i, predictions_array, true_label, img):
    true_label, img = true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img, cmap=plt.cm.binary)


def plot_value_array(i, predictions_array, true_label):
    true_label = true_label[i]
    plt.grid(False)
    plt.xticks(range(10))
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)

    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')


def check_prediction(index, predictions, test_labels, test_images):
    print(predictions[index])
    print(np.argmax(predictions[index]))
    print(np.argmax(predictions[index]) == test_labels[index])
    plt.figure(figsize=(6, 3))
    plt.subplot(1, 2, 1)
    plot_image(index, predictions[index], test_labels, test_images)
    # plt.subplot(1,2,2)
    # plot_value_array(index, predictions[index],  test_labels)
    plt.show()


def evaluate_model(X_train, X_test, y_train, y_test, model, kana):
    # data augmentation, we use shifting and zoom here
    datagen = tf.keras.preprocessing.image.ImageDataGenerator(rotation_range=5, width_shift_range=0.3, height_shift_range=0.3)
    datagen.fit(X_train)

    history = model.fit(datagen.flow(X_train, y_train, shuffle=True), epochs=EPOCHS, validation_data=(X_test, y_test),
                        callbacks=[tf.keras.callbacks.EarlyStopping(patience=8, verbose=0, restore_best_weights=True),
                                   tf.keras.callbacks.ReduceLROnPlateau(factor=0.5, patience=3, verbose=0)])
    
    _, acc = model.evaluate(X_test, y_test, verbose=0)
    print('> %.3f' % (acc * 100.0))
    
    # save model if the accuracy above 97%
    if (acc * 100.0) > ACCURACY_ACCEPTED:
        probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
        predictions = probability_model.predict(X_test)
        check_prediction(10, predictions, y_test, X_test)
        probability_model.save(kana + "_model")

    scores, histories = list(), list()
    scores.append(acc)
    histories.append(history)
    return scores, histories


def summarize_diagnostic_learning_curves(histories):
    for i in range(len(histories)):
        # plot loss
        plt.subplot(2, 1, 1)
        plt.title('Cross Entropy Loss')
        plt.plot(histories[i].history['loss'], color='blue', label='train')
        plt.plot(histories[i].history['val_loss'], color='orange', label='test')
        # plot accuracy
        plt.subplot(2, 1, 2)
        plt.title('Classification Accuracy')
        plt.plot(histories[i].history['accuracy'], color='blue', label='train')
        plt.plot(histories[i].history['val_accuracy'], color='orange', label='test')
    plt.legend()
    plt.show()
    plt.savefig('evaluation', format='png')


def summarize_estimated_model_performance(scores):
    print('Accuracy: mean=%.3f std=%.3f, n=%d' % (mean(scores)*100, std(scores)*100, len(scores)))
    # box and whisker plots of results
    # plt.boxplot(scores)
    # plt.show()



###############################################################################
# optimization for cpu (you can comment if you're using gpu)
# https://software.intel.com/content/www/us/en/develop/articles/guide-to-tensorflow-runtime-optimizations-for-cpu.html
###############################################################################

tf.config.threading.set_inter_op_parallelism_threads(16)
tf.config.threading.set_intra_op_parallelism_threads(16)
tf.config.set_soft_device_placement(True)

###############################################################################
# execute cnn
###############################################################################

def execute_cnn(kana):
    print("--- "+kana)
    
    x_df, y_df, quantity = load_npz(kana)

    X_train, X_test, y_train, y_test = train_test_split(x_df, y_df, test_size=0.2)
    X_train = X_train.reshape(X_train.shape[0], TRAIN_SQUARE_SIZE_X, TRAIN_SQUARE_SIZE_Y, 1)
    X_test = X_test.reshape(X_test.shape[0], TRAIN_SQUARE_SIZE_X, TRAIN_SQUARE_SIZE_Y, 1)

    model = define_model(quantity)

    scores, histories = evaluate_model(X_train, X_test, y_train, y_test, model, kana)

    summarize_diagnostic_learning_curves(histories)

    summarize_estimated_model_performance(scores)


with tf.device('/cpu:0'):
	print("=== execute cnn started")
	execute_cnn(HIRAGANA)
	#execute_cnn(KATAKANA)
	print("=== execute cnn started")
