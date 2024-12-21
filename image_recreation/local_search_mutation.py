
import time
import numpy as np
from PIL import Image
from image_recreation.generatePng import generatePng
from image_recreation.fitness import compute_fitness
from image_recreation.crossover_genotypes import generate_random_genotype
from image_recreation.mutate_genotype import mutate_genotype

def run_local_search_with_mutation(input_image_path, shape, n, output_image_path, max_iterations=3, mutation_rate=0.1):
    """
    Implémente une recherche locale avec mutation pour trouver une solution optimale.

    Arguments :
    - input_image_path : chemin de l'image cible.
    - shape : type de forme géométrique.
    - n : nombre de formes.
    - output_image_path : chemin de sortie pour l'image SVG/PNG.
    - max_iterations : nombre maximum d'itérations pour la recherche.
    - mutation_rate : taux de mutation (entre 0 et 1).

    Retourne :
    - best_genotype : génotype de la meilleure solution.
    - best_fitness : valeur de fitness associée.
    """
    # Charger l'image cible
    target_image = Image.open(input_image_path)
    width, height = target_image.size

    # Initialisation
    best_genotype = generate_random_genotype(n, shape)
    best_fitness = float('inf')
    start_time = time.time()
    for iteration in range(max_iterations):
        # Appliquer une mutation sur le génotype
        mutated_genotype = mutate_genotype(best_genotype, mutation_rate)

        # Générer une image PNG à partir du génotype muté
        generated_png_path = output_image_path.split(".")[0] + f"_local_mutation_{iteration}.png"
        generatePng(genotype=mutated_genotype, output=generated_png_path, width=width, height=height)

        # Calculer la fitness de la solution mutée
        fitness = compute_fitness(generated_png_path, input_image_path)
        #calcul du temps
        elapsed_time = time.time() - start_time
        print(f"Itération {iteration + 1}/{max_iterations} - Fitness : {fitness}")

        # Vérifier si c'est la meilleure solution
        if fitness < best_fitness:
            best_fitness = fitness
            best_genotype = mutated_genotype

    print(f"Meilleure fitness trouvée : {best_fitness}")

    # Générer un PNG final pour la meilleure solution
    final_png_path = output_image_path.split(".")[0] + "_best_local_mutation.png"
    generatePng(genotype=best_genotype, output=final_png_path, width=width, height=height)

    return best_genotype, best_fitness
