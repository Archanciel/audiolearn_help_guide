// lib/viewmodels/help_categories_viewmodel.dart

import 'package:flutter/material.dart';
import '../models/help_category.dart';

class HelpCategoriesViewModel extends ChangeNotifier {
  final List<HelpCategory> _categories = [];

  List<HelpCategory> get categories => _categories;

  HelpCategoriesViewModel() {
    _initializeCategories();
  }

  void _initializeCategories() {
    _categories.addAll([
      HelpCategory(
        id: 'introduction',
        title: 'Introduction d\'Audio Learn',
        description: 'Définir, ajouter et télécharger une playlist YouTube',
        icon: Icons.play_circle_outline,
        jsonFilePath: 'assets/help/french/playlist_usage/help_content.json',
      ),
      HelpCategory(
        id: 'menu_playlist',
        title: 'Menu Playlist',
        description: 'Fonctionnalités du menu playlist',
        icon: Icons.playlist_play,
        jsonFilePath: 'assets/help/french/menu_playlist/help_content.json',
      ),
      HelpCategory(
        id: 'menu_audio',
        title: 'Menu Audio',
        description: 'Fonctionnalités du menu audio',
        icon: Icons.audiotrack,
        jsonFilePath: 'assets/help/french/menu_audio/help_content.json',
      ),
    ]);
  }

  HelpCategory? getCategoryById(String categoryId) {
    try {
      return _categories.firstWhere((category) => category.id == categoryId);
    } catch (e) {
      return null;
    }
  }
}