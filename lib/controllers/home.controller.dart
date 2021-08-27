import 'dart:ui';

import 'package:flutter/material.dart';
import 'package:tensorflow_kana_recognizer/controllers/kana.dart';
import 'package:tensorflow_kana_recognizer/controllers/kana.interface.repository.dart';
import 'package:tensorflow_kana_recognizer/controllers/kana_recognizer.interface.service.dart';
import 'package:tensorflow_kana_recognizer/models/kana.repository.dart';
import 'package:tensorflow_kana_recognizer/models/kana_recognizer.service.dart';

class HomeController {
  HomeController() {
    _hiraganaRecognizer = KanaRecognizerService(KanaType.hiragana);
    _katakanaRecognizer = KanaRecognizerService(KanaType.katakana);
    _repository = KanaRepository();
    kanaToWrite = _repository.getRandomKana();
  }

  late final IKanaRepository _repository;
  late final IKanaRecognizerService _hiraganaRecognizer;
  late final IKanaRecognizerService _katakanaRecognizer;

  double startSquareLimit = 0.0;
  double endSquareLimit = 100.0;
  bool _isCorrect = false;
  String _charWrote = '';

  List<List<Offset>> strokes = [];
  late Kana kanaToWrite;

  void addStroke(List<Offset> stroke) {
    strokes.add(stroke);
  }

  void clearStrokes() {
    strokes.clear();
  }

  void undoTheLastStroke() {
    if (strokes.isNotEmpty) {
      strokes.removeLast();
    }
  }

  bool get isTheLastStroke => strokes.length >= kanaToWrite.maxStrokes;

  String get showMessageTop => 'Write: ${kanaToWrite.id}';

  String get showMessageBottom => _isCorrect
      ? 'Wrote correct: $_charWrote'
      : _charWrote.isNotEmpty
          ? 'Wrote wrong: $_charWrote'
          : '';

  Future<void> updateKana() async {
    final normalizedPicture = _pointsToPicture();

    List<dynamic>? listPrediction;
    if (kanaToWrite.kanaType.isHiragana) {
      listPrediction = await _hiraganaRecognizer.recognize(normalizedPicture);
    } else {
      listPrediction = await _katakanaRecognizer.recognize(normalizedPicture);
    }

    print(listPrediction);
    if (listPrediction!.isEmpty) {
      _isCorrect = false;
      _charWrote = '';
    } else {
      final kanaId = listPrediction.elementAt(0);
      _isCorrect = kanaToWrite.id == kanaId['label'];
      _charWrote = kanaId['label'] as String;
      print('waiting for:${kanaToWrite.id} what recognized: ${kanaId['label']} type: ${kanaToWrite.kanaType.toString()}');
    }

    kanaToWrite = _repository.getRandomKana();
    strokes.clear();
  }

  void dispose() {
    _hiraganaRecognizer.dispose();
    _katakanaRecognizer.dispose();
  }

  Picture _pointsToPicture() {
    const canvasSize = 100.0;
    final strokePaint = Paint()
      ..strokeCap = StrokeCap.round
      ..color = Colors.white
      ..strokeWidth = 5;
    final backgroundPaint = Paint()..color = Colors.black;

    final canvasRect = Rect.fromPoints(Offset(startSquareLimit, startSquareLimit), Offset(endSquareLimit, endSquareLimit));
    final recorder = PictureRecorder();
    final canvas = Canvas(recorder, canvasRect)..scale(KanaRecognizerService.imageDataSize / canvasSize);

    canvas.drawRect(Rect.fromPoints(Offset.zero, const Offset(canvasSize, canvasSize)), backgroundPaint);

    for (final points in strokes) {
      canvas.drawPoints(PointMode.polygon, points, strokePaint);
    }
    return recorder.endRecording();
  }
}
