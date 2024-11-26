import argparse
from image_recreation.utils.clearConsole import clearConsole
from image_recreation.utils.verifyShape import verifyShape
from image_recreation.utils.svg_tags.svg_circle_tag import svg_circle_tag
from image_recreation.utils.svg_tags.svg_rect_tag import svg_rect_tag
from image_recreation.utils.svg_tags.svg_ellipse_tag import svg_ellipse_tag
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

print(svg_circle_tag(100,50,75,127,134,83))
print(svg_rect_tag(10,20,100,100,52,30,34))
print(svg_ellipse_tag(10,20,25,50,127,134,83))
print(width)

svg_openTag = f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" version="1.1">'
svg_closeTag = "</svg>"
svg_all_line = ""



# for x in range(width):

#     for y in range(height):
#         red, green, blue = input_image.getpixel((x, y))# recuperation des pixels de la position (x,y)
#         svg_all_line = svg_all_line + svg_circle_tag(cx=x, cy=y, rayon=50, red=red, green=green, blue=blue)


for x in range(args.n):
    y = args.n
    
    red, green, blue = input_image.getpixel((x, y))# recuperation des pixels de la position (x,y)
    svg_all_line = svg_all_line + svg_circle_tag(cx=x, cy=y, rayon=100, red=red, green=green, blue=blue)


# # Écrire le contenu dans un fichier
with open(args.output, "w") as svg_file:
    svg_file.write(svg_openTag +  svg_all_line + svg_closeTag)

# print("Image SVG créée : 'example.svg'")
