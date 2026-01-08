// lib/viewmodels/help_guide_viewmodel.dart

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'dart:convert';
import '../models/help_step.dart';
import '../models/help_section.dart';

class HelpGuideViewModel extends ChangeNotifier {
  List<HelpStep> _allSteps = [];
  List<HelpSection> _sections = [];
  bool _isLoading = true;
  String? _errorMessage;

  List<HelpStep> get allSteps => _allSteps;
  List<HelpSection> get sections => _sections;
  bool get isLoading => _isLoading;
  String? get errorMessage => _errorMessage;

  HelpGuideViewModel() {
    _initializeSections();
    _loadHelpContent();
  }

  void _initializeSections() {
    _sections = [
      HelpSection(
        id: 'create_playlist',
        title: 'Créer une Playlist YouTube',
        description: 'Apprenez à créer une playlist YouTube Non répertoriée ou Publique',
        icon: Icons.playlist_add,
        startStep: 1,
        endStep: 9,
      ),
      HelpSection(
        id: 'download_playlist',
        title: 'Télécharger la Playlist',
        description: 'Téléchargez les audios de votre playlist dans l\'application',
        icon: Icons.download,
        startStep: 10,
        endStep: 24,
      ),
      HelpSection(
        id: 'download_single',
        title: 'Télécharger une Vidéo Unique',
        description: 'Téléchargez l\'audio d\'une seule vidéo YouTube',
        icon: Icons.video_library,
        startStep: 25,
        endStep: 26,
      ),
    ];
  }

  Future<void> _loadHelpContent() async {
    try {
      _isLoading = true;
      _errorMessage = null;
      notifyListeners();

      final String jsonString = 
          await rootBundle.loadString('assets/help/help_content.json');
      final List<dynamic> jsonData = json.decode(jsonString);

      _allSteps = jsonData.map((json) => HelpStep.fromJson(json)).toList();

      _isLoading = false;
      notifyListeners();
    } catch (e) {
      _isLoading = false;
      _errorMessage = 'Erreur lors du chargement du guide: $e';
      notifyListeners();
    }
  }

  List<HelpStep> getStepsForSection(String sectionId) {
    return _allSteps.where((step) => step.sectionId == sectionId).toList();
  }

  HelpSection? getSectionById(String sectionId) {
    try {
      return _sections.firstWhere((section) => section.id == sectionId);
    } catch (e) {
      return null;
    }
  }

  Future<void> reload() async {
    await _loadHelpContent();
  }
}
