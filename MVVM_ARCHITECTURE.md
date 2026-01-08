# 🏗️ Architecture MVVM - AudioLearn Help Guide

## 📐 Vue d'Ensemble

Cette application utilise le pattern **MVVM (Model-View-ViewModel)** pour une séparation claire des responsabilités.

```
┌─────────────────────────────────────────────────────────┐
│                     INTERFACE UTILISATEUR                │
│                          (VIEW)                          │
│  ┌───────────────────────────────────────────────────┐  │
│  │  HelpTableOfContentsScreen                        │  │
│  │  - Affiche la table des matières                  │  │
│  │  - Liste les 3 sections                           │  │
│  └──────────────┬────────────────────────────────────┘  │
│                 │                                        │
│  ┌──────────────▼────────────────────────────────────┐  │
│  │  HelpStepsScreen                                  │  │
│  │  - Affiche les étapes avec PageView               │  │
│  │  - Gère la navigation entre les pages             │  │
│  └──────────────┬────────────────────────────────────┘  │
└─────────────────┼────────────────────────────────────────┘
                  │
                  │ observe & notify
                  │
┌─────────────────▼────────────────────────────────────────┐
│                      LOGIQUE MÉTIER                       │
│                       (VIEWMODEL)                         │
│  ┌───────────────────────────────────────────────────┐  │
│  │  HelpGuideViewModel (ChangeNotifier)              │  │
│  │  - Charge le JSON                                 │  │
│  │  - Gère la liste des étapes                       │  │
│  │  - Gère la liste des sections                     │  │
│  │  - Gère l'état de chargement                      │  │
│  └──────────────┬────────────────────────────────────┘  │
│                 │                                        │
│  ┌──────────────▼────────────────────────────────────┐  │
│  │  HelpPageViewModel (ChangeNotifier)               │  │
│  │  - Gère le PageController                         │  │
│  │  - Suit la page courante                          │  │
│  │  - Navigation Précédent/Suivant                   │  │
│  └──────────────┬────────────────────────────────────┘  │
└─────────────────┼────────────────────────────────────────┘
                  │
                  │ accède aux données
                  │
┌─────────────────▼────────────────────────────────────────┐
│                         DONNÉES                           │
│                         (MODEL)                           │
│  ┌───────────────────────────────────────────────────┐  │
│  │  HelpStep                                         │  │
│  │  - stepNumber                                     │  │
│  │  - sectionId                                      │  │
│  │  - imagePath                                      │  │
│  │  - title                                          │  │
│  │  - description                                    │  │
│  └───────────────────────────────────────────────────┘  │
│                                                          │
│  ┌───────────────────────────────────────────────────┐  │
│  │  HelpSection                                      │  │
│  │  - id                                             │  │
│  │  - title                                          │  │
│  │  - description                                    │  │
│  │  - icon                                           │  │
│  │  - startStep / endStep                            │  │
│  └───────────────────────────────────────────────────┘  │
└───────────────────────────────────────────────────────────┘
```

---

## 🔄 Flux de Données

### 1️⃣ Chargement Initial

```
┌──────────────────┐
│  Application     │
│  démarre         │
└────────┬─────────┘
         │
         ▼
┌────────────────────────────────┐
│  HelpGuideViewModel            │
│  • Charge help_content.json    │
│  • Parse le JSON               │
│  • Crée List<HelpStep>         │
│  • notifyListeners()           │
└────────┬───────────────────────┘
         │
         ▼
┌────────────────────────────────┐
│  HelpTableOfContentsScreen     │
│  • Observe le ViewModel        │
│  • Affiche les sections        │
│  • Attend interaction          │
└────────────────────────────────┘
```

### 2️⃣ Navigation vers une Section

```
┌────────────────────────────────┐
│  Utilisateur clique            │
│  sur "Créer une Playlist"      │
└────────┬───────────────────────┘
         │
         ▼
┌────────────────────────────────┐
│  HelpTableOfContentsScreen     │
│  • getStepsForSection()        │
│  • Navigator.push()            │
└────────┬───────────────────────┘
         │
         ▼
┌────────────────────────────────┐
│  HelpStepsScreen               │
│  • Crée HelpPageViewModel      │
│  • Reçoit List<HelpStep>       │
│  • Affiche PageView            │
└────────────────────────────────┘
```

### 3️⃣ Navigation entre Pages

```
┌────────────────────────────────┐
│  Utilisateur swipe / clique    │
│  "Suivant"                     │
└────────┬───────────────────────┘
         │
         ▼
┌────────────────────────────────┐
│  NavigationButtons             │
│  • Appelle onNext()            │
└────────┬───────────────────────┘
         │
         ▼
┌────────────────────────────────┐
│  HelpPageViewModel             │
│  • pageController.nextPage()   │
│  • _currentPage++              │
│  • notifyListeners()           │
└────────┬───────────────────────┘
         │
         ▼
┌────────────────────────────────┐
│  UI se met à jour              │
│  • PageIndicator               │
│  • NavigationButtons           │
│  • AppBar title                │
└────────────────────────────────┘
```

---

## 📦 Responsabilités par Couche

### 🎨 VIEW (Interface)

**Fichiers** :
- `help_table_of_contents_screen.dart`
- `help_steps_screen.dart`
- `help_step_page.dart`
- `page_indicator.dart`
- `navigation_buttons.dart`

**Responsabilités** :
- ✅ Afficher l'interface utilisateur
- ✅ Capturer les interactions
- ✅ Observer les ViewModels
- ✅ Se mettre à jour automatiquement
- ❌ PAS de logique métier
- ❌ PAS d'accès direct aux données

**Exemple** :
```dart
Consumer<HelpGuideViewModel>(
  builder: (context, viewModel, child) {
    if (viewModel.isLoading) {
      return CircularProgressIndicator();
    }
    return ListView(
      children: viewModel.sections.map((section) => 
        SectionCard(section: section)
      ).toList(),
    );
  },
)
```

---

### 🧠 VIEWMODEL (Logique)

**Fichiers** :
- `help_guide_viewmodel.dart`
- `help_page_viewmodel.dart`

**Responsabilités** :
- ✅ Gère l'état de l'application
- ✅ Charge et traite les données
- ✅ Expose les données à la View
- ✅ Gère les erreurs
- ✅ Notifie les changements (ChangeNotifier)
- ❌ PAS de référence à Flutter UI
- ❌ PAS de BuildContext

**Exemple** :
```dart
class HelpGuideViewModel extends ChangeNotifier {
  List<HelpStep> _allSteps = [];
  bool _isLoading = true;
  
  Future<void> _loadHelpContent() async {
    _isLoading = true;
    notifyListeners();  // UI se met à jour
    
    final data = await loadJson();
    _allSteps = parseSteps(data);
    
    _isLoading = false;
    notifyListeners();  // UI se met à jour
  }
}
```

---

### 📊 MODEL (Données)

**Fichiers** :
- `help_step.dart`
- `help_section.dart`

**Responsabilités** :
- ✅ Définit la structure des données
- ✅ Sérialisation JSON (fromJson/toJson)
- ✅ Validation des données
- ❌ PAS de logique métier
- ❌ PAS d'interaction UI

**Exemple** :
```dart
class HelpStep {
  final int stepNumber;
  final String title;
  
  HelpStep({
    required this.stepNumber,
    required this.title,
  });
  
  factory HelpStep.fromJson(Map<String, dynamic> json) {
    return HelpStep(
      stepNumber: json['stepNumber'],
      title: json['title'],
    );
  }
}
```

---

## 🔗 Communication entre Couches

### Provider Pattern

```dart
// Dans main.dart ou au niveau racine
ChangeNotifierProvider(
  create: (_) => HelpGuideViewModel(),
  child: HelpTableOfContentsScreen(),
)

// Dans la View
Consumer<HelpGuideViewModel>(
  builder: (context, viewModel, child) {
    return Text(viewModel.someData);
  },
)

// Ou
final viewModel = Provider.of<HelpGuideViewModel>(context);
```

---

## ✅ Avantages de MVVM

### 1. Séparation des Préoccupations
- ✅ UI distincte de la logique
- ✅ Code plus maintenable
- ✅ Plus facile à tester

### 2. Testabilité
- ✅ ViewModels testables sans UI
- ✅ Models testables indépendamment
- ✅ Mocks faciles à créer

### 3. Réutilisabilité
- ✅ ViewModels réutilisables
- ✅ Models partagés
- ✅ Widgets composables

### 4. Scalabilité
- ✅ Facile d'ajouter des features
- ✅ Code organisé
- ✅ Équipe peut travailler en parallèle

---

## 🧪 Tests

### Test d'un Model
```dart
test('HelpStep fromJson creates valid object', () {
  final json = {
    'stepNumber': 1,
    'title': 'Test',
  };
  
  final step = HelpStep.fromJson(json);
  
  expect(step.stepNumber, 1);
  expect(step.title, 'Test');
});
```

### Test d'un ViewModel
```dart
test('HelpGuideViewModel loads data correctly', () async {
  final viewModel = HelpGuideViewModel();
  
  await viewModel.loadHelpContent();
  
  expect(viewModel.allSteps.length, 26);
  expect(viewModel.isLoading, false);
});
```

---

## 📚 Ressources

- [Provider Documentation](https://pub.dev/packages/provider)
- [MVVM Pattern](https://en.wikipedia.org/wiki/Model–view–viewmodel)
- [Flutter Architecture](https://flutter.dev/docs/development/data-and-backend/state-mgmt)

---

## 🎯 En Résumé

```
MODEL       ➡️  Définit les données
   ⬇️
VIEWMODEL   ➡️  Gère la logique + l'état
   ⬇️
VIEW        ➡️  Affiche et capture l'interaction
```

**Règle d'or** : Chaque couche ne dépend que de celle en dessous !
