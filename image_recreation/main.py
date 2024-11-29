import argparse
import random
from image_recreation.utils.clearConsole import clearConsole
from image_recreation.utils.verifyShape import verifyShape
from image_recreation.utils.svg_tags.svg_circle_tag import svg_circle_tag
from image_recreation.utils.svg_tags.svg_rect_tag import svg_rect_tag
from image_recreation.utils.svg_tags.svg_ellipse_tag import svg_ellipse_tag
from image_recreation.generateSvg import generateSvg
from image_recreation.generatePng import generatePng
from PIL import Image
import math
# Créer l'analyseur d'arguments
parser = argparse.ArgumentParser(description='-------Recuperation des input------\n')

# Ajouter des arguments
parser.add_argument('--input', type=str, required=True, help="l'image a transformer")
parser.add_argument('--shape', type=str, required=True, help="la forme de la figure")
parser.add_argument('--n', type=int, required=True, help="le nombre de figure a utiliser")
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

print("***************PROCESS DE TRAITEMENT INITIE****************\n")

#appel de la function pour générer le phenotype
generateSvg(input_image=input_image, shape=args.shape, n=args.n, width=width, height=height,output=args.output)
genotype=generateSvg(input_image=input_image, shape=args.shape, n=args.n, width=width, height=height, output=args.output, isPng=True)
generatePng(genotype=genotype,output=args.output,width=width,height=height)

