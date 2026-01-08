# 🚀 Guide d'Intégration Rapide dans AudioLearn

## Étape 1 : Ajouter vos images (26 images)

Placez vos images extraites du PDF dans :
```
audiolearn_help_guide/assets/help/images/
```

Nommez-les correctement :
- `step_01.jpg`
- `step_02.jpg`
- ...
- `step_26.jpg`

## Étape 2 : Tester l'Application Autonome

```bash
cd audiolearn_help_guide
flutter pub get
flutter run -d windows  # ou android
```

## Étape 3 : Intégrer dans AudioLearn

### A. Copier les Fichiers

```bash
# Dans votre projet AudioLearn, créez les dossiers
mkdir -p lib/help/models
mkdir -p lib/help/viewmodels
mkdir -p lib/help/views
mkdir -p lib/help/widgets
mkdir -p assets/help/images

# Copiez les fichiers
cp audiolearn_help_guide/lib/models/* YOUR_AUDIOLEARN/lib/help/models/
cp audiolearn_help_guide/lib/viewmodels/* YOUR_AUDIOLEARN/lib/help/viewmodels/
cp audiolearn_help_guide/lib/views/* YOUR_AUDIOLEARN/lib/help/views/
cp audiolearn_help_guide/lib/widgets/* YOUR_AUDIOLEARN/lib/help/widgets/
cp audiolearn_help_guide/assets/help/* YOUR_AUDIOLEARN/assets/help/
cp -r audiolearn_help_guide/assets/help/images/* YOUR_AUDIOLEARN/assets/help/images/
```

### B. Modifier pubspec.yaml

Dans votre projet AudioLearn, ajoutez :

```yaml
dependencies:
  provider: ^6.1.1  # Si pas déjà présent

flutter:
  assets:
    - assets/help/help_content.json
    - assets/help/images/
```

### C. Ajouter un Bouton dans votre Interface

**Option 1 : Dans l'AppBar**

```dart
import 'package:flutter/material.dart';
import 'help/views/help_table_of_contents_screen.dart';

// Dans votre AppBar
AppBar(
  title: Text('AudioLearn'),
  actions: [
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
    ),
  ],
)
```

**Option 2 : Dans le Drawer (Menu Latéral)**

```dart
Drawer(
  child: ListView(
    children: [
      // ... autres items
      ListTile(
        leading: Icon(Icons.help_outline),
        title: Text('Guide d\'utilisation'),
        onTap: () {
          Navigator.pop(context); // Fermer le drawer
          Navigator.push(
            context,
            MaterialPageRoute(
              builder: (context) => HelpTableOfContentsScreen(),
            ),
          );
        },
      ),
    ],
  ),
)
```

**Option 3 : Bouton Flottant**

```dart
FloatingActionButton(
  onPressed: () {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => HelpTableOfContentsScreen(),
      ),
    );
  },
  child: Icon(Icons.help),
  tooltip: 'Guide d\'utilisation',
)
```

### D. Ajouter les Imports Nécessaires

Dans le fichier où vous voulez le bouton d'aide :

```dart
import 'package:flutter/material.dart';
import 'help/views/help_table_of_contents_screen.dart';
```

## Étape 4 : Compiler et Tester

```bash
flutter pub get
flutter run
```

## ✅ Checklist de Vérification

- [ ] 26 images copiées dans `assets/help/images/`
- [ ] Fichiers Dart copiés dans `lib/help/`
- [ ] `help_content.json` copié dans `assets/help/`
- [ ] `pubspec.yaml` mis à jour
- [ ] `provider` ajouté aux dépendances
- [ ] Bouton d'aide ajouté dans l'interface
- [ ] Import de `help_table_of_contents_screen.dart`
- [ ] `flutter pub get` exécuté
- [ ] Application testée sur Windows
- [ ] Application testée sur Android

## 🎯 Utilisation dans l'Application

1. Cliquez sur le bouton d'aide (icône `?`)
2. Choisissez une section dans la table des matières
3. Naviguez entre les étapes :
   - **Swipe** gauche/droite
   - Boutons **Précédent**/**Suivant**
   - **Liste** des étapes (icône en haut)
4. **Pincez** pour zoomer sur les images

## 🔧 Personnalisation des Couleurs

Dans `main.dart` de votre AudioLearn, vous pouvez définir les couleurs :

```dart
MaterialApp(
  theme: ThemeData(
    primarySwatch: Colors.blue,  // Votre couleur principale
    // ...
  ),
)
```

## 🐛 Résolution de Problèmes Fréquents

### Erreur : "The asset ... does not exist"

```bash
flutter clean
flutter pub get
```

### Erreur : "Provider not found"

```bash
flutter pub add provider
```

### Images trop grandes / trop petites

Les images s'adaptent automatiquement grâce à `InteractiveViewer` et `fit: BoxFit.contain`.
Si besoin, modifiez dans `help_step_page.dart` :

```dart
maxHeight: MediaQuery.of(context).size.height * 0.70,  // 70% au lieu de 60%
```

## 📞 Support

Si vous rencontrez des problèmes, vérifiez :
1. Que tous les fichiers sont copiés
2. Que `pubspec.yaml` est correct
3. Que les 26 images sont présentes
4. Que `flutter pub get` a été exécuté

Bon développement ! 🎉
