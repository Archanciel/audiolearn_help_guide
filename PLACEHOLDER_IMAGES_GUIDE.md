# 🖼️ Images Placeholder pour Tester l'Application

Si vous voulez tester l'application **AVANT** d'avoir vos vraies images, voici comment créer des images placeholder.

## Option 1 : Utiliser un Service en Ligne (Recommandé)

### Via Placeholder.com

Téléchargez 26 images avec :
```
https://via.placeholder.com/600x1200/0066cc/ffffff?text=Etape+1
https://via.placeholder.com/600x1200/0066cc/ffffff?text=Etape+2
...
https://via.placeholder.com/600x1200/0066cc/ffffff?text=Etape+26
```

Renommez-les en `step_01.jpg`, `step_02.jpg`, etc.

---

## Option 2 : Script Python pour Générer des Placeholders

```python
#!/usr/bin/env python3
"""
Génère 26 images placeholder pour tester l'application.
Nécessite: pip install Pillow
"""

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

def create_placeholder_image(step_number, output_path):
    """Crée une image placeholder pour une étape."""
    # Dimensions (format smartphone vertical)
    width, height = 600, 1200
    
    # Couleur de fond
    bg_color = (0, 102, 204)  # Bleu
    text_color = (255, 255, 255)  # Blanc
    
    # Créer l'image
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Texte
    text = f"Étape {step_number}"
    
    # Essayer de charger une police, sinon utiliser la police par défaut
    try:
        font = ImageFont.truetype("arial.ttf", 80)
        font_small = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Centrer le texte principal
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # Dessiner le texte principal
    draw.text((x, y), text, fill=text_color, font=font)
    
    # Texte secondaire
    subtitle = "Image Placeholder"
    bbox_sub = draw.textbbox((0, 0), subtitle, font=font_small)
    text_width_sub = bbox_sub[2] - bbox_sub[0]
    x_sub = (width - text_width_sub) // 2
    y_sub = y + text_height + 40
    
    draw.text((x_sub, y_sub), subtitle, fill=text_color, font=font_small)
    
    # Sauvegarder
    img.save(output_path, 'JPEG', quality=85)
    print(f"✅ Créé: {output_path.name}")


def main():
    """Génère toutes les images placeholder."""
    output_folder = Path("assets/help/images")
    output_folder.mkdir(parents=True, exist_ok=True)
    
    print("🖼️  Génération de 26 images placeholder...")
    print()
    
    for i in range(1, 27):
        filename = f"step_{i:02d}.jpg"
        output_path = output_folder / filename
        create_placeholder_image(i, output_path)
    
    print()
    print("🎉 Terminé! 26 images créées dans assets/help/images/")
    print()
    print("💡 Vous pouvez maintenant tester l'application avec:")
    print("   flutter run")


if __name__ == "__main__":
    print("=" * 60)
    print("  GÉNÉRATEUR D'IMAGES PLACEHOLDER - AUDIOLEARN HELP")
    print("=" * 60)
    print()
    main()
```

### Utilisation du Script

```bash
# Installer Pillow
pip install Pillow

# Lancer le script depuis la racine du projet
python scripts/create_placeholder_images.py

# Ou si vous êtes dans le dossier scripts :
cd scripts
python create_placeholder_images.py
```

---

## Option 3 : Images Simples avec Paint (Windows)

1. Ouvrez **Paint**
2. Créez une image **600 x 1200 pixels**
3. Remplissez avec une couleur
4. Ajoutez du texte : "Étape 1", "Étape 2", etc.
5. Enregistrez comme `step_01.jpg`, `step_02.jpg`, etc.

---

## Option 4 : Utiliser GIMP (Gratuit)

1. **Fichier** → **Nouvelle image**
2. **Largeur**: 600, **Hauteur**: 1200
3. **Remplir avec**: Couleur de premier plan
4. **Texte** → Ajoutez "Étape X"
5. **Fichier** → **Exporter sous** → `step_XX.jpg`

---

## Vérification

Après création, vérifiez :

```bash
ls assets/help/images/ | wc -l
# Devrait afficher : 26
```

---

## Testez l'Application

```bash
flutter run -d windows
```

Vous devriez voir :
- ✅ Table des matières avec 3 sections
- ✅ Navigation entre les étapes
- ✅ Images placeholder avec "Étape X"
- ✅ Zoom fonctionnel

---

## Remplacer par les Vraies Images

Quand vous avez vos vraies captures d'écran :

1. **Supprimez** les placeholders :
   ```bash
   rm assets/help/images/*.jpg
   ```

2. **Copiez** vos vraies images :
   ```bash
   cp /chemin/vers/vos/images/*.jpg assets/help/images/
   ```

3. **Relancez** l'application :
   ```bash
   flutter run
   ```

---

## Tailles Recommandées

Pour de vraies captures d'écran Android :
- **Format portrait** (vertical)
- **Largeur** : 400-800 px
- **Qualité** : 70-85%
- **Format** : JPG ou PNG

L'application redimensionnera automatiquement les images pour qu'elles s'affichent correctement.

---

## 💡 Conseil

Utilisez les placeholders pour :
- ✅ Tester la navigation
- ✅ Vérifier le design
- ✅ Tester sur Windows et Android
- ✅ Développer d'autres fonctionnalités

Puis remplacez par vos vraies images quand vous êtes prêt !
