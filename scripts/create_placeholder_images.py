#!/usr/bin/env python3
"""
Génère 26 images placeholder pour tester l'application AudioLearn Help Guide.
Nécessite: pip install Pillow
Utilisation: python create_placeholder_images.py
"""

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import sys


def create_placeholder_image(step_number, output_path):
    """
    Crée une image placeholder pour une étape donnée.
    
    Args:
        step_number: Numéro de l'étape (1-26)
        output_path: Chemin de sortie pour l'image
    """
    # Dimensions (format smartphone vertical)
    width, height = 600, 1200
    
    # Couleurs
    bg_color = (0, 102, 204)  # Bleu AudioLearn
    text_color = (255, 255, 255)  # Blanc
    
    # Créer l'image
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Texte principal
    main_text = f"Étape {step_number}"
    
    # Essayer de charger une police, sinon utiliser la police par défaut
    try:
        # Windows
        font_large = ImageFont.truetype("arial.ttf", 80)
        font_medium = ImageFont.truetype("arial.ttf", 40)
        font_small = ImageFont.truetype("arial.ttf", 30)
    except:
        try:
            # Linux
            font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)
            font_medium = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
            font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
        except:
            # Police par défaut
            font_large = ImageFont.load_default()
            font_medium = ImageFont.load_default()
            font_small = ImageFont.load_default()
    
    # Centrer le texte principal
    bbox = draw.textbbox((0, 0), main_text, font=font_large)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (width - text_width) // 2
    y = (height - text_height) // 2 - 50
    
    # Dessiner le texte principal
    draw.text((x, y), main_text, fill=text_color, font=font_large)
    
    # Texte secondaire
    subtitle = "Image Placeholder"
    bbox_sub = draw.textbbox((0, 0), subtitle, font=font_medium)
    text_width_sub = bbox_sub[2] - bbox_sub[0]
    x_sub = (width - text_width_sub) // 2
    y_sub = y + text_height + 40
    
    draw.text((x_sub, y_sub), subtitle, fill=text_color, font=font_medium)
    
    # Texte en bas
    bottom_text = "AudioLearn Help Guide"
    bbox_bottom = draw.textbbox((0, 0), bottom_text, font=font_small)
    text_width_bottom = bbox_bottom[2] - bbox_bottom[0]
    x_bottom = (width - text_width_bottom) // 2
    y_bottom = height - 100
    
    draw.text((x_bottom, y_bottom), bottom_text, fill=text_color, font=font_small)
    
    # Dessiner un cadre
    border_width = 10
    draw.rectangle(
        [(border_width, border_width), (width - border_width, height - border_width)],
        outline=(255, 255, 255),
        width=border_width
    )
    
    # Sauvegarder
    img.save(output_path, 'JPEG', quality=85)
    print(f"  ✅ Créé: {output_path.name}")


def main():
    """Génère toutes les images placeholder."""
    # Déterminer le dossier de sortie
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    output_folder = project_root / "assets" / "help" / "images"
    
    # Créer le dossier s'il n'existe pas
    output_folder.mkdir(parents=True, exist_ok=True)
    
    print("🖼️  GÉNÉRATION D'IMAGES PLACEHOLDER")
    print("=" * 60)
    print()
    print(f"📁 Dossier de sortie: {output_folder}")
    print(f"📊 Nombre d'images: 26")
    print()
    
    # Générer les 26 images
    for i in range(1, 27):
        filename = f"step_{i:02d}.jpg"
        output_path = output_folder / filename
        create_placeholder_image(i, output_path)
    
    print()
    print("=" * 60)
    print("🎉 Terminé! 26 images créées avec succès!")
    print()
    print("💡 Prochaines étapes:")
    print("   1. Vérifiez les images dans:", output_folder)
    print("   2. Testez l'application: flutter run")
    print("   3. Remplacez par vos vraies images quand vous êtes prêt")
    print()


if __name__ == "__main__":
    print()
    try:
        from PIL import Image
    except ImportError:
        print("❌ Erreur: Pillow n'est pas installé!")
        print()
        print("📦 Installez-le avec:")
        print("   pip install Pillow")
        print()
        sys.exit(1)
    
    main()
