import argparse
import numpy as np
import random
from image_recreation.local_search_mutation import run_local_search_with_mutation
from image_recreation.utils.clearConsole import clearConsole
from image_recreation import local_search
from image_recreation.utils.verifyShape import verifyShape
from image_recreation.utils.svg_tags.svg_circle_tag import svg_circle_tag
from image_recreation.utils.svg_tags.svg_rect_tag import svg_rect_tag
from image_recreation.utils.svg_tags.svg_ellipse_tag import svg_ellipse_tag
from image_recreation.generateSvg import generateSvg
from image_recreation.generatePng import generatePng
from image_recreation.mutate_genotype import mutate_genotype
from image_recreation.crossover_genotypes import crossover_genotypes
from image_recreation.crossover_genotypes import generate_random_genotype
from image_recreation.local_search import run_local_search
from image_recreation.fitness import compute_fitness 
from PIL import Image

import math
# Créer l'analyseur d'arguments
parser = argparse.ArgumentParser(description='-------Recuperation des input------\n')

# Ajouter des arguments
parser.add_argument('--input', type=str, required=True, help="l'image a transformer")
parser.add_argument('--shape', type=str, required=True, help="la forme de la figure")
parser.add_argument('--n', type=int, required=True, help="le nombre de figure a utiliser")
parser.add_argument('--iterations', type=str, required=True, help="Nombre d'itérations ")
parser.add_argument('--method', type=str, required=True, choices=['random', 'local'], help="Méthode de métaheuristique à utiliser")
parser.add_argument('--output', type=str, required=True, help="l'image transformée")

# Analyser les arguments
args = parser.parse_args()

# # Ouvrir l'image d'entrée
input_image = Image.open(args.input)

# Obtenir les dimensions de l'image
width, height = input_image.size

# Obtenir le format de l'image 
imageFormat = input_image.format

# Clear the console
clearConsole()

# exit the program if shape is not autorized 
verifyShape(args.shape)

# affichage des arguments
print(f'Votre image a transformer: {args.input} \n')
print(f'la forme des figure choisi: {args.shape} \n')
print(f'le nombre de figure a utiliser: {args.n}')
print(f'Fichier de sortie l\'image transformée: {args.output} \n')
print(width,height)
print("***************PROCESS DE TRAITEMENT INITIE****************\n")

#appel de la function pour générer le phenotype
generateSvg(input_image=input_image, shape=args.shape, n=args.n, width=width, height=height,output=args.output)
genotype=generateSvg(input_image=input_image, shape=args.shape, n=args.n, width=width, height=height, output=args.output, isPng=False)
# Générer le PNG correspondant
png_output_path = args.output.split(".")[0] + ".png"
generatePng(genotype=genotype, output=png_output_path, width=width, height=height)

#Computing a fitness value from a phenotype

# Chemin des images pour la fitness
generated_image_path = png_output_path # Image générée
target_image_path = args.input      # Image cible

# Calculer la fitness
try:
    fitness = compute_fitness(generated_image_path, target_image_path)
    print(f"Fitness de l'image générée : {fitness}")
except ValueError as e:
    print(f"Erreur lors du calcul de la fitness : {e}")

# Mutation sur le génotype
mutated_genotype = mutate_genotype(genotype, mutation_rate=0.2)

# Générer un nouveau PNG à partir du génotype muté
mutated_png_output = args.output.split(".")[0] + "_mutated.png"
generatePng(genotype=mutated_genotype, output=mutated_png_output, width=width, height=height)

# Calculer la fitness du génotype muté
mutated_fitness = compute_fitness(mutated_png_output, target_image_path)

print(f"Fitness après mutation : {mutated_fitness}")

#crossover genotypes

genotype1= generate_random_genotype(1000, "circle")
genotype2=generate_random_genotype(1000,"rect")
#print("Parent 1 (genotype1):", genotype1)
#print("Parent 2 (genotype2):", genotype2)
child_genotype=crossover_genotypes(genotype1,genotype2)
#print("Enfant généré :", child_genotype)
# Générer un nouveau PNG à partir du crossover
crossover_png_output = args.output.split(".")[0] + "crossover.png"
generatePng(genotype=child_genotype, output=crossover_png_output, width=width, height=height)

#exécution de  local search
run_local_search(input_image_path=args.input, shape=args.shape, n=args.n, output_image_path=args.output, max_iterations=args.iterations)
# Exécution de  la métaheuristique choisie
if args.method == 'random':
    run_local_search(input_image_path=args.input, shape=args.shape, n=args.n, output_image_path=args.output, max_iterations=args.iterations)
elif args.method == 'local': 
    run_local_search_with_mutation(input_image_path=args.input, shape=args.shape, n=args.n, output_image_path=args.output, max_iterations=args.iterations, mutation_rate=0.1)

# Exécuter la recherche aléatoire
print("Exécution de la recherche aléatoire...")
best_genotype_random, best_fitness_random = run_local_search(input_image_path=args.input, shape=args.shape, n=args.n, output_image_path=args.output, max_iterations=args.iterations)

# Exécuter la recherche locale avec mutation
print("Exécution de la recherche locale avec mutation...")
best_genotype_local, best_fitness_local = run_local_search_with_mutation(input_image_path=args.input, shape=args.shape, n=args.n, output_image_path=args.output, max_iterations=args.iterations, mutation_rate=0.1)

# Comparer les résultats
print(f"Meilleure fitness (Recherche Aléatoire) : {best_fitness_random}")
print(f"Meilleure fitness (Recherche Locale avec Mutation) : {best_fitness_local}")
 