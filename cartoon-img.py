import cv2
from PIL import Image
import numpy as np

def cartoonize_image(image_path, output_path="avatar.png"):
    # Charger l’image
    img = cv2.imread(image_path)
    img = cv2.resize(img, (256, 256))  # Taille standard d’un avatar

    # Convertir en gris
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 7)

    # Détection des bords
    edges = cv2.adaptiveThreshold(gray, 255,
                                   cv2.ADAPTIVE_THRESH_MEAN_C,
                                   cv2.THRESH_BINARY, 9, 9)

    # Appliquer un filtre bilateral (effet "lissé")
    color = cv2.bilateralFilter(img, d=9, sigmaColor=250, sigmaSpace=250)

    # Fusionner les bords avec l’image colorée
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # Sauvegarder
    cv2.imwrite(output_path, cartoon)

    # Affichage (optionnel avec PIL)
    Image.open(output_path).show()

# Utilisation
cartoonize_image("img/image.jpeg")  # Remplacer par ton image source
