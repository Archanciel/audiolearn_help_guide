# 🖼️ Guide d'Extraction des Images du PDF

## Méthode 1 : Utiliser le Script Python (Recommandé)

### Prérequis

```bash
pip install PyMuPDF
```

### Utilisation

1. **Placez votre PDF** dans le dossier `audiolearn_help_guide/scripts/`
   - Nom du fichier : `Utilisation_d_AudioLearn_pour_ajouter_une_playlist_Youtube_dans_l_application.pdf`

2. **Exécutez le script** :

```bash
cd audiolearn_help_guide/scripts
python extract_images_from_pdf.py
```

3. **Les images extraites** seront dans `scripts/extracted_images/`
   - Nommées : `step_01.jpg`, `step_02.jpg`, ..., `step_26.jpg`

4. **Copiez les images** dans le dossier assets :

```bash
cp extracted_images/* ../assets/help/images/
```

---

## Méthode 2 : Extraction Manuelle depuis Google Docs

### Sur ordinateur :

1. Ouvrez le document dans **Google Docs**
2. Pour chaque image :
   - Clic droit → **Enregistrer dans Keep** ou **Télécharger**
   - Ou : Clic droit → **Copier l'image** → Collez dans un logiciel → Enregistrez

3. Renommez les images :
   - `step_01.jpg`
   - `step_02.jpg`
   - ...
   - `step_26.jpg`

### Sur Android :

1. Ouvrez le document dans **Google Docs**
2. Appui long sur chaque image
3. **Enregistrer l'image**
4. Renommez dans votre gestionnaire de fichiers
5. Transférez vers votre PC si nécessaire

---

## Méthode 3 : Depuis les Captures d'Écran que Vous Avez

Si vous avez déjà les 26 captures d'écran originales :

1. **Renommez-les** simplement :
   ```
   20260106_180724_temp.jpg  → step_01.jpg
   [votre_deuxième_image].jpg → step_02.jpg
   ...
   ```

2. **Placez-les** dans :
   ```
   audiolearn_help_guide/assets/help/images/
   ```

---

## Vérification

Après extraction, vérifiez que vous avez :

```
assets/help/images/
├── step_01.jpg
├── step_02.jpg
├── step_03.jpg
├── ...
└── step_26.jpg
```

**Commande pour compter** :
```bash
ls assets/help/images/ | wc -l
```

Devrait afficher : `26`

---

## Format des Images

- **Format accepté** : `.jpg`, `.jpeg`, `.png`
- **Taille recommandée** : Largeur 400-800px (les grandes images seront redimensionnées automatiquement)
- **Qualité** : Moyenne à bonne (pas besoin de haute résolution)

---

## Problèmes Courants

### Script Python ne fonctionne pas

```bash
# Installer PyMuPDF
pip install PyMuPDF

# Ou avec pip3
pip3 install PyMuPDF
```

### PDF non trouvé

Assurez-vous que le PDF est dans le même dossier que le script :
```
scripts/
├── extract_images_from_pdf.py
└── Utilisation_d_AudioLearn_pour_ajouter_une_playlist_Youtube_dans_l_application.pdf
```

### Images de mauvaise qualité

Le script extrait les images telles qu'elles sont dans le PDF. Si la qualité est mauvaise, utilisez plutôt les captures d'écran originales.

---

## Conseil

💡 **Utilisez vos captures d'écran originales** si vous les avez toujours !
Elles seront de meilleure qualité que les images extraites du PDF.
