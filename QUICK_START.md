# ⚡ Démarrage Rapide - AudioLearn Help Guide

## 🎯 Objectif
Application Flutter MVVM affichant un guide interactif avec vos 26 captures d'écran du processus AudioLearn.

---

## 📦 Ce que vous avez

```
audiolearn_help_guide/
├── lib/                           # Code Flutter (MVVM)
│   ├── models/                    # Modèles de données
│   ├── viewmodels/               # Logique métier (MVVM)
│   ├── views/                    # Écrans
│   └── widgets/                  # Composants réutilisables
├── assets/
│   └── help/
│       ├── help_content.json     # Configuration des 26 étapes
│       └── images/               # ⚠️ À REMPLIR avec vos 26 images
├── scripts/
│   └── extract_images_from_pdf.py  # Script d'extraction (optionnel)
└── README.md                     # Documentation complète
```

---

## 🚀 3 Étapes pour Démarrer

### 1️⃣ Ajoutez vos 26 images

```bash
# Placez vos images dans ce dossier :
audiolearn_help_guide/assets/help/images/

# Noms requis :
step_01.jpg
step_02.jpg
step_03.jpg
...
step_26.jpg
```

💡 **Astuce** : Si vous avez le PDF, utilisez le script Python dans `scripts/`

### 2️⃣ Installez les dépendances

```bash
cd audiolearn_help_guide
flutter pub get
```

### 3️⃣ Lancez l'application

**Windows :**
```bash
flutter run -d windows
```

**Android :**
```bash
flutter devices              # Listez vos appareils
flutter run -d <device_id>   # Lancez sur l'appareil choisi
```

---

## ✨ Fonctionnalités

### 📚 Table des Matières
- 3 sections thématiques
- Navigation par cartes
- Compteur d'étapes

### 📖 Visualisation
- PageView (swipe gauche/droite)
- Zoom sur images (pinch)
- Boutons Précédent/Suivant
- Liste des étapes accessible

### 🎨 Design
- Mode clair/sombre automatique
- Responsive (Windows + Android)
- Indicateurs de progression

---

## 🔗 Intégrer dans AudioLearn

### Méthode Simple

Dans votre `main.dart` ou écran principal d'AudioLearn :

```dart
import 'package:flutter/material.dart';
// Ajoutez cette ligne après avoir copié les fichiers :
import 'help/views/help_table_of_contents_screen.dart';

// Quelque part dans votre interface :
IconButton(
  icon: Icon(Icons.help_outline),
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

### Fichiers à Copier

```bash
# Copiez dans votre projet AudioLearn :
lib/help/              # Tout le code du guide
assets/help/           # JSON + images
```

### Dépendance à Ajouter

Dans `pubspec.yaml` :
```yaml
dependencies:
  provider: ^6.1.1  # Si pas déjà présent
```

---

## 📖 Documentation Complète

| Fichier | Description |
|---------|-------------|
| `README.md` | Documentation complète du projet |
| `INTEGRATION_GUIDE.md` | Guide détaillé d'intégration dans AudioLearn |
| `IMAGE_EXTRACTION_GUIDE.md` | Comment extraire les images du PDF |
| `STEPS_REFERENCE.md` | Liste des 26 étapes du guide |

---

## 🎯 Workflow Recommandé

1. ✅ **Testez l'app autonome** d'abord
   ```bash
   flutter run -d windows
   ```

2. ✅ **Vérifiez que tout fonctionne** :
   - Images s'affichent
   - Navigation fonctionne
   - Zoom fonctionne

3. ✅ **Intégrez dans AudioLearn** :
   - Copiez les fichiers
   - Ajoutez le bouton d'aide
   - Testez

---

## 🐛 Problèmes Fréquents

### Images ne s'affichent pas
```bash
flutter clean
flutter pub get
```

### Provider not found
```bash
flutter pub add provider
```

### Erreur "Asset not found"
Vérifiez `pubspec.yaml` :
```yaml
flutter:
  assets:
    - assets/help/help_content.json
    - assets/help/images/
```

---

## 📱 Architecture MVVM

```
┌─────────────────┐
│     View        │  ← Interface utilisateur
│  (Screens)      │
└────────┬────────┘
         │
┌────────▼────────┐
│   ViewModel     │  ← Logique métier + État
│ (ChangeNotifier)│
└────────┬────────┘
         │
┌────────▼────────┐
│     Model       │  ← Données
│  (HelpStep)     │
└─────────────────┘
```

---

## 🎉 C'est Prêt !

Votre guide interactif AudioLearn est maintenant :
- ✅ Compatible Windows et Android
- ✅ Architecture MVVM propre
- ✅ Facilement intégrable
- ✅ Personnalisable

**Bonne intégration ! 🚀**
