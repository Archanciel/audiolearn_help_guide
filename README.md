# AudioLearn - Guide d'utilisation (Application Flutter MVVM)

Cette application Flutter fournit un guide interactif pas-à-pas pour utiliser AudioLearn. Elle utilise l'architecture MVVM et est compatible **Windows** et **Android**.

## 📁 Structure du Projet

```
audiolearn_help_guide/
├── lib/
│   ├── main.dart                          # Point d'entrée de l'application
│   ├── models/
│   │   ├── help_step.dart                 # Modèle pour une étape
│   │   └── help_section.dart              # Modèle pour une section
│   ├── viewmodels/
│   │   ├── help_guide_viewmodel.dart      # ViewModel principal
│   │   └── help_page_viewmodel.dart       # ViewModel pour la navigation
│   ├── views/
│   │   ├── help_table_of_contents_screen.dart  # Table des matières
│   │   └── help_steps_screen.dart         # Écran des étapes
│   └── widgets/
│       ├── help_step_page.dart            # Widget pour une page d'étape
│       ├── page_indicator.dart            # Indicateur de page
│       └── navigation_buttons.dart        # Boutons de navigation
├── assets/
│   └── help/
│       ├── help_content.json              # Contenu du guide
│       └── images/                        # Images des étapes (step_01.jpg à step_26.jpg)
└── pubspec.yaml                           # Dépendances du projet
```

## 🚀 Installation et Exécution

### 1. Prérequis
- Flutter SDK (>=3.0.0)
- Dart SDK
- Un éditeur (VS Code, Android Studio, etc.)

### 2. Installation des dépendances

```bash
cd audiolearn_help_guide
flutter pub get
```

### 3. Ajouter vos images

Placez vos 26 images dans le dossier :
```
assets/help/images/
```

Nommez-les : `step_01.jpg`, `step_02.jpg`, ..., `step_26.jpg`

### 4. Exécuter l'application

**Sur Windows :**
```bash
flutter run -d windows
```

**Sur Android :**
```bash
flutter run -d <device_id>
```

**Liste des appareils connectés :**
```bash
flutter devices
```

## 📱 Fonctionnalités

### Table des Matières
- **3 sections** organisées par thème
- Navigation intuitive avec cartes cliquables
- Compteur d'étapes par section
- Design responsive

### Visualisation des Étapes
- **PageView** pour navigation fluide (swipe gauche/droite)
- **InteractiveViewer** pour zoomer sur les images (pinch to zoom)
- Indicateur de progression
- Liste des étapes accessible via bouton
- Navigation avec boutons Précédent/Suivant

### Sections du Guide

1. **Créer une Playlist YouTube** (8 étapes)
   - Comment créer une playlist
   - Définir la visibilité (Non répertoriée/Publique)

2. **Ajouter la Playlist dans AudioLearn** (16 étapes)
   - Copier le lien YouTube
   - Ajouter dans l'application
   - Télécharger les audios

3. **Télécharger une Vidéo Unique** (2 étapes)
   - Partager une vidéo
   - Télécharger l'audio

## 🔧 Intégration dans AudioLearn

### Option 1 : Module Autonome

Copiez les dossiers dans votre projet AudioLearn :

```bash
# Copier les fichiers
cp -r audiolearn_help_guide/lib/* YOUR_AUDIOLEARN_PROJECT/lib/help/
cp -r audiolearn_help_guide/assets/* YOUR_AUDIOLEARN_PROJECT/assets/
```

Ajoutez dans votre `pubspec.yaml` :
```yaml
dependencies:
  provider: ^6.1.1

flutter:
  assets:
    - assets/help/help_content.json
    - assets/help/images/
```

### Option 2 : Bouton d'Aide dans AudioLearn

Ajoutez un bouton dans votre interface principale :

```dart
// Dans votre AppBar ou Drawer
IconButton(
  icon: Icon(Icons.help_outline),
  tooltip: 'Guide d\'utilisation',
  onPressed: () {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => HelpTableOfContentsScreen(),
      ),
    );
  },
)
```

### Option 3 : Menu Contextuel

```dart
PopupMenuButton<String>(
  onSelected: (value) {
    if (value == 'help') {
      Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) => HelpTableOfContentsScreen(),
        ),
      );
    }
  },
  itemBuilder: (context) => [
    PopupMenuItem(
      value: 'help',
      child: Row(
        children: [
          Icon(Icons.help),
          SizedBox(width: 8),
          Text('Guide d\'utilisation'),
        ],
      ),
    ),
  ],
)
```

## 📝 Personnalisation

### Modifier le Contenu

Éditez `assets/help/help_content.json` :

```json
{
  "stepNumber": 27,
  "sectionId": "download_single",
  "imagePath": "assets/help/images/step_27.jpg",
  "title": "Nouvelle étape",
  "description": "Description de la nouvelle étape..."
}
```

### Ajouter une Section

Dans `help_guide_viewmodel.dart` :

```dart
HelpSection(
  id: 'nouvelle_section',
  title: 'Nouvelle Section',
  description: 'Description de la section',
  icon: Icons.new_releases,
  startStep: 27,
  endStep: 30,
),
```

### Changer les Couleurs

Dans `main.dart`, modifiez le `ThemeData` :

```dart
theme: ThemeData(
  primarySwatch: Colors.green,  // Votre couleur
  // ...
),
```

## 🎨 Captures d'Écran

L'application affiche :
- **Table des matières** avec 3 sections
- **Pages d'étapes** avec images zoomables
- **Navigation** intuitive
- **Indicateurs de progression**

## 📦 Dépendances

- **flutter** : Framework principal
- **provider** : Gestion d'état (MVVM)

## ⚙️ Compatibilité

- ✅ **Windows** (Desktop)
- ✅ **Android** (Mobile/Tablet)
- ✅ **iOS** (non testé mais devrait fonctionner)
- ✅ **Web** (non testé mais devrait fonctionner)

## 🐛 Résolution de Problèmes

### Images ne s'affichent pas

1. Vérifiez que les images sont dans `assets/help/images/`
2. Vérifiez les noms : `step_01.jpg` à `step_26.jpg`
3. Vérifiez `pubspec.yaml` :
   ```yaml
   flutter:
     assets:
       - assets/help/images/
   ```
4. Exécutez : `flutter clean && flutter pub get`

### Erreur "Asset not found"

```bash
flutter clean
flutter pub get
flutter run
```

### Provider not found

```bash
flutter pub add provider
```

## 📄 Licence

Ce projet est créé pour AudioLearn. Tous droits réservés.

## 👨‍💻 Auteur

Créé avec ❤️ pour Jean-Pierre
