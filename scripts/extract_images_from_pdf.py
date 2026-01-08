#!/usr/bin/env python3
"""
Script pour extraire les images du PDF AudioLearn et les renommer correctement.
Utilisation: python extract_images_from_pdf.py
"""

import fitz  # PyMuPDF
import os
from pathlib import Path

def extract_images_from_pdf(pdf_path, output_folder):
    """
    Extrait toutes les images d'un PDF et les sauvegarde avec des noms séquentiels.
    
    Args:
        pdf_path: Chemin vers le fichier PDF
        output_folder: Dossier de destination pour les images
    """
    # Créer le dossier de sortie s'il n'existe pas
    output_path = Path(output_folder)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Ouvrir le PDF
    doc = fitz.open(pdf_path)
    print(f"📄 PDF ouvert: {pdf_path}")
    print(f"📊 Nombre de pages: {len(doc)}")
    
    image_count = 0
    
    # Parcourir toutes les pages
    for page_num in range(len(doc)):
        page = doc[page_num]
        images = page.get_images()
        
        print(f"\n📃 Page {page_num + 1}: {len(images)} image(s) trouvée(s)")
        
        # Extraire chaque image de la page
        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            
            # Incrémenter le compteur
            image_count += 1
            
            # Nom du fichier de sortie
            image_filename = f"step_{image_count:02d}.jpg"
            image_path = output_path / image_filename
            
            # Sauvegarder l'image
            with open(image_path, "wb") as img_file:
                img_file.write(image_bytes)
            
            print(f"  ✅ Extrait: {image_filename} ({len(image_bytes) // 1024} KB)")
    
    doc.close()
    
    print(f"\n🎉 Extraction terminée!")
    print(f"📁 {image_count} images extraites dans: {output_folder}")
    print(f"\n💡 Prochaine étape:")
    print(f"   Copiez ces images dans: audiolearn_help_guide/assets/help/images/")


def main():
    """Point d'entrée principal du script."""
    # Configuration
    pdf_filename = "Utilisation_d_AudioLearn_pour_ajouter_une_playlist_Youtube_dans_l_application.pdf"
    output_folder = "extracted_images"
    
    # Vérifier si le PDF existe
    if not os.path.exists(pdf_filename):
        print(f"❌ Erreur: Le fichier '{pdf_filename}' n'existe pas!")
        print(f"📝 Assurez-vous que le PDF est dans le même dossier que ce script.")
        return
    
    # Extraire les images
    try:
        extract_images_from_pdf(pdf_filename, output_folder)
    except Exception as e:
        print(f"\n❌ Erreur lors de l'extraction: {e}")
        print(f"💡 Assurez-vous d'avoir installé PyMuPDF: pip install PyMuPDF")


if __name__ == "__main__":
    print("=" * 70)
    print("🖼️  EXTRACTEUR D'IMAGES PDF POUR AUDIOLEARN")
    print("=" * 70)
    print()
    main()
    print()
    print("=" * 70)
