# Tensorflow Kana Recognizer

This is a project made in Flutter for kana recognition by drawing the user's strokes using Tensorflow to recognize the drawn kana.

<p align="center">
 <a href="#important-note">Important Note</a> •
 <a href="#about-the-project">About the project</a> •
 <a href="#technologies">Technologies</a> • 
 <a href="#license">License</a>
</p>

## Important Note

This project was abandoned. My intention for this project was to create a kana recognition system using Tensorflow to work on another larger Flutter project, but with the low number of correct responses in kana recognition, I decided to look for another way to recognize kana, because creating this algorithm didn't was my main focus.

The problem with this algorithm is that when drawing the は, the predictions came something like ば or even ぱ, reaching a recognition probability greater than 90%. With basic knowledge about Machine Learning, management of incompatible versions of tensorflow packages and low efficiency in training (algorithm takes time to run) using a virtual machine for Ubuntu, I couldn't find the real problem because I was generating this inconsistent information, so I decided to abandon this project.

As I studied and generated some knowledge, I decided to post here in case someone wants to reuse it, even if it was not a success for me.

## About the project

The project makes it possible to draw a kana on the screen and tensorflow recognizes the drawing and predicts which kana you have written.

By drawing the strokes on the screen, it is able to generate the image, which is sent to the Tflite library, which recognizes which kana was drawn.

Scripts are written in python. It is numbered for the recommended order of execution.

Scripts 1, 2 and 3 are for extracting kanas from Japanese fonts and generating png images.

Scripts 4, 5 and 6 are for compressing the images, training and generating the database by Tensorflow.

I prepared the script to generate the database for hiragana and katakana, being 2 separate files, because when together they could give many false positives like the HE of hiragana and katakana.

The project was based on the [jayndu](https://jaycoding.tech/tutorials/guides/efficient-sketching-app-using-flutter-icstum) and the [Hiragana recognizer app](https://github.com/thomasoca/hiragana_recognizer_app).

The algorithm for generating the Tensorflow database was based on [Hiragana recognizer cnn](https://github.com/thomasoca/hiragana-recognizer-cnn).

To generate the images of the kanas to train the Tensorflow database, I used the same strategy as the project [Hiragata ai](https://github.com/Orzelius/Hiragata_ai), which used free fonts of Japanese letters, usually of the handwriting type.

Other data to train the Tensorflow database were taken from [ELT](http://etlcdb.db.aist.go.jp/). These data have restrictions for commercial use, so enter the site for more information if you want to use their data.

## Technologies

<p><img alt="Dart" src="https://img.shields.io/badge/Dart-2.13.4-03589b?style=for-the-badge&logo=dart">
<img alt="Flutter" src="https://img.shields.io/badge/Flutter-2.2.3-53c5f7?style=for-the-badge&logo=flutter"></p>
<p><img alt="Python" src="https://img.shields.io/badge/Python-3.8.10-fadf5e?style=for-the-badge&logo=python">
<img alt="Tensorflow" src="https://img.shields.io/badge/Tensorflow-2.5.0-fadf5e?style=for-the-badge">
<img alt="FontForge" src="https://img.shields.io/badge/font forge-20201107-fadf5e?style=for-the-badge">
<img alt="Pillow" src="https://img.shields.io/badge/pillow-7.0.0-fadf5e?style=for-the-badge">
<img alt="scikit-image" src="https://img.shields.io/badge/scikit image-0.18.2-fadf5e?style=for-the-badge">
<img alt="scikit-learn" src="https://img.shields.io/badge/scikit learn-0.24.2-fadf5e?style=for-the-badge"></p>

## License

The license is in accordance with MIT, however, while not mandatory, I would like you to cite that the code was based on this project.
