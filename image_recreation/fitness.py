

import numpy as np
from PIL import Image

def compute_fitness(generated_image_path, target_image_path):
    # Ouvrir les images
    img1 = Image.open(generated_image_path)
    img2 = Image.open(target_image_path)

    # Convertir les images en tableaux numpy
    img1_array = np.array(img1)
    img2_array = np.array(img2)

    # Vérifier que les dimensions des deux images correspondent
    if img1_array.shape != img2_array.shape:
        raise ValueError("Les dimensions des deux images ne correspondent pas.")
    
    # Calculer l'écart entre les pixels des deux images (différence absolue)
    diff = np.abs(img1_array - img2_array)

    # Calculer le nombre total de pixels
    total_pixel = img1_array.shape[0] * img1_array.shape[1]

    # Somme des différences
    fitness_total = np.sum(diff)
    fitness_value = fitness_total / total_pixel
    
    return fitness_value
