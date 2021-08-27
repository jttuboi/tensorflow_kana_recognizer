import 'package:tensorflow_kana_recognizer/models/kana_recognizer.service.dart';

class Kana {
  Kana(this.id, this.kanaType, this.maxStrokes);

  final String id;
  final KanaType kanaType;
  final int maxStrokes;
}
