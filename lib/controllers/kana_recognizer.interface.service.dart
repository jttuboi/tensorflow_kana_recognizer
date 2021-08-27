import 'dart:ui';

abstract class IKanaRecognizerService {
  Future<List<dynamic>?> recognize(Picture picture);

  void dispose();
}
