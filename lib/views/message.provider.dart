import 'package:flutter/foundation.dart';
import 'package:tensorflow_kana_recognizer/controllers/home.controller.dart';

class MessageProvider extends ChangeNotifier {
  MessageProvider(this._controller);

  final HomeController _controller;

  String get messageTop => _controller.showMessageTop;

  String get messageBottom => _controller.showMessageBottom;

  bool get isTheLastStroke => _controller.isTheLastStroke;

  String get kanaId => _controller.kanaToWrite.id;

  Future<void> updateMessage() async {
    // if calling to update message, so all the strokes are drawn
    await _controller.updateKana();
    notifyListeners();
  }
}
