// lib/main.dart

import 'dart:io';

import 'package:flutter/material.dart';
import 'package:window_size/window_size.dart';
import 'views/widgets/help_categories_screen.dart';

Future<void> main() async {
  WidgetsFlutterBinding
      .ensureInitialized(); // Ensure Flutter bindings are initialized.

  // Now proceed with setting up the app window size and position if needed
  if (Platform.isWindows || Platform.isLinux || Platform.isMacOS) {
    await _setWindowsAppSizeAndPosition(
      isTest: true,
      // isTest: false,
    );
  }

  runApp(const AudioLearnHelpApp());
}

/// If app runs on Windows, Linux or MacOS, set the app size
/// and position.
Future<void> _setWindowsAppSizeAndPosition({
  required bool isTest,
}) async {
  await getScreenList().then((List<Screen> screens) {
    // Assumez que vous voulez utiliser le premier écran (principal)
    final Screen screen = screens.first;
    final Rect screenRect = screen.visibleFrame;

    // Définissez la largeur et la hauteur de votre fenêtre
    double windowWidth = (isTest) ? 900 : 730;
    double windowHeight = (isTest) ? 1700 : 1480;

    // Calculez la position X pour placer la fenêtre sur le côté droit de l'écran
    final double posX = screenRect.right - windowWidth + 10;
    // Optionnellement, ajustez la position Y selon vos préférences
    final double posY = (screenRect.height - windowHeight) / 2;

    final Rect windowRect =
        Rect.fromLTWH(posX, posY, windowWidth, windowHeight);
    setWindowFrame(windowRect);
  });
}

class AudioLearnHelpApp extends StatelessWidget {
  const AudioLearnHelpApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'AudioLearn - Aide',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blue,
        brightness: Brightness.light,
        scaffoldBackgroundColor: Colors.grey[100],
        appBarTheme: const AppBarTheme(
          elevation: 0,
          centerTitle: true,
          backgroundColor: Colors.blue,
          foregroundColor: Colors.white,
        ),
        cardTheme: CardThemeData(
          elevation: 2,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(12),
          ),
        ),
        elevatedButtonTheme: ElevatedButtonThemeData(
          style: ElevatedButton.styleFrom(
            elevation: 2,
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(8),
            ),
          ),
        ),
      ),
      darkTheme: ThemeData(
        primarySwatch: Colors.blue,
        brightness: Brightness.dark,
        scaffoldBackgroundColor: Colors.grey[900],
        appBarTheme: AppBarTheme(
          elevation: 0,
          centerTitle: true,
          backgroundColor: Colors.grey[850],
        ),
        cardTheme: CardThemeData(
          elevation: 2,
          color: Colors.grey[850],
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(12),
          ),
        ),
        elevatedButtonTheme: ElevatedButtonThemeData(
          style: ElevatedButton.styleFrom(
            elevation: 2,
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(8),
            ),
          ),
        ),
      ),
      themeMode: ThemeMode.system,
      home: const HelpCategoriesScreen(),
    );
  }
}