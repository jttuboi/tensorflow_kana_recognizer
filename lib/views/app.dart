import 'package:flutter/material.dart';
import 'package:tensorflow_kana_recognizer/views/home.page.dart';

class App extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(primarySwatch: Colors.blue),
      home: HomePage(),
    );
  }
}
