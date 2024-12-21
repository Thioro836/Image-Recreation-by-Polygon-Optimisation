import time
import numpy as np
from PIL import Image
from image_recreation.generatePng import generatePng
from image_recreation.fitness import compute_fitness
from image_recreation.crossover_genotypes import generate_random_genotype

def run_local_search(input_image_path, shape, n, output_image_path, max_iterations=3):
    """
    Implémente une recherche locale pour trouver une solution optimale.

    Arguments :
    - input_image_path : chemin de l'image cible.
    - shape : type de forme géométrique.
    - n : nombre de formes.
    - output_image_path : chemin de sortie pour l'image SVG/PNG.
    - max_iterations : nombre maximum d'itérations pour la recherche.

    Retourne :
    - best_genotype : génotype de la meilleure solution.
    - best_fitness : valeur de fitness associée.
    """
    # Charger l'image cible
    target_image = Image.open(input_image_path)
    width, height = target_image.size

    # Initialisation
    best_genotype = None
    best_fitness = float('inf')
    start_time = time.time()
    
    for iteration in range(max_iterations):
        # Générer un génotype aléatoire
        genotype = generate_random_genotype(n, shape)

        # Générer une image PNG à partir du génotype
        generated_png_path = output_image_path.split(".")[0] + f"_local_{iteration}.png"
        generatePng(genotype=genotype, output=generated_png_path, width=width, height=height)

        # Calculer la fitness de la solution
        fitness = compute_fitness(generated_png_path, input_image_path)
        #calcul du temps
        elapsed_time = time.time() - start_time
        print(f"Itération {iteration + 1}/{max_iterations} - Fitness : {fitness}")

        # Vérifier si c'est la meilleure solution
        if fitness < best_fitness:
            best_fitness = fitness
            best_genotype = genotype

    print(f"Meilleure fitness trouvée : {best_fitness}")

    # Générer un PNG final pour la meilleure solution
    final_png_path = output_image_path.split(".")[0] + "_best_local.png"
    generatePng(genotype=best_genotype, output=final_png_path, width=width, height=height)

    return best_genotype, best_fitness

# recherche local avec mutation

