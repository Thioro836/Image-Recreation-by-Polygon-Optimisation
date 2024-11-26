import argparse
from PIL import Image
import  numpy as np
from image_recreation.testModule import bonjour

bonjour()
# Créer l'analyseur d'arguments
# parser = argparse.ArgumentParser(description='Un exemple de programme avec argparse')

# # Ajouter des arguments
# parser.add_argument('--input', type=str, required=True, help='Le fichier d\'entrée')
# parser.add_argument('--output', type=str, required=True, help='Le fichier de sortie')

# # Analyser les arguments
# args = parser.parse_args()

# # Accéder aux arguments
# print(f'Fichier d\'entrée: {args.input}')
# print(f'Fichier de sortie: {args.output}')

# # Ouvrir l'image d'entrée
# input_image = Image.open(args.input).convert('RGB')

# image_np=np.array(input_image)
# print (image_np)

# print(input_image)
# print(input_image.size)
# print(input_image.format)
# # Créer une nouvelle image de la même taille pour la sortie
# output_image = Image.new('RGB', input_image.size,(224,224,224))
# output_image.save(args.output)

# Obtenir les dimensions de l'image
# width, height = input_image.size

# # recuperer les pixels
# for x in range(width):
#     for y in range(height):
#         pixel = input_image.getpixel((x, y ))
#         output_image.putpixel((x, y), pixel)
#type attendu

