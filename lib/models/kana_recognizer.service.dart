import 'dart:typed_data';
import 'dart:ui';

import 'package:tensorflow_kana_recognizer/controllers/kana_recognizer.interface.service.dart';
import 'package:tflite/tflite.dart';

enum KanaType { hiragana, katakana }

extension KanaTypeExtension on KanaType {
  bool get isHiragana => this == KanaType.hiragana;
  bool get isKatakana => this == KanaType.katakana;
}

class KanaRecognizerService implements IKanaRecognizerService {
  KanaRecognizerService(KanaType kanaType) {
    Tflite.close();

    if (kanaType.isHiragana) {
      Tflite.loadModel(
        model: 'lib/assets/hiragana.tflite',
        labels: 'lib/assets/hiragana.txt',
        numThreads: 2,
      );
    } else {
      // TODO you need change to katakana model
      Tflite.loadModel(
        model: 'lib/assets/hiragana__hiragana_recognizer_app_version.tflite',
        labels: 'lib/assets/hiragana__hiragana_recognizer_app_version.txt',
        numThreads: 2,
      );
    }
  }

  static const imageDataSize = 32;
  static const quantityOfResults = 10;

  @override
  Future<List<dynamic>?> recognize(Picture picture) async {
    final bytes = await _imageToByteListUint8(picture, imageDataSize);
    return Tflite.runModelOnBinary(binary: bytes, numResults: quantityOfResults, threshold: 0.05);
  }

  @override
  void dispose() {
    Tflite.close();
  }

  Future<Uint8List> _imageToByteListUint8(Picture pic, int size) async {
    final img = await pic.toImage(size, size);
    final imgBytes = await img.toByteData();
    final resultBytes = Float32List(size * size);
    final buffer = Float32List.view(resultBytes.buffer);

    int index = 0;

    for (int i = 0; i < imgBytes!.lengthInBytes; i += 4) {
      final r = imgBytes.getUint8(i);
      final g = imgBytes.getUint8(i + 1);
      final b = imgBytes.getUint8(i + 2);
      buffer[index++] = (r + g + b) / 3.0 / 255.0;
    }

    return resultBytes.buffer.asUint8List();
  }
}
