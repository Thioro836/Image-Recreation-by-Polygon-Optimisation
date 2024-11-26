import argparse
from image_recreation.utils.clearConsole import clearConsole
from image_recreation.utils.verifyShape import verifyShape
from image_recreation.utils.svg_tags.svg_circle_tag import svg_circle_tag
from image_recreation.utils.svg_tags.svg_rect_tag import svg_rect_tag
from image_recreation.utils.svg_tags.svg_ellipse_tag import svg_ellipse_tag
from PIL import Image
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

print(svg_circle_tag(100,50,75,127,134,83))
print(svg_rect_tag(10,20,100,100,52,30,34))
print(svg_ellipse_tag(10,20,25,50,127,134,83))
