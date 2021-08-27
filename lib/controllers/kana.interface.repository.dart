import 'package:tensorflow_kana_recognizer/controllers/kana.dart';

abstract class IKanaRepository {
  Kana getRandomKana();
}
