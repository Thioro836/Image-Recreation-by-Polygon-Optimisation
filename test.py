# # Contenu SVG sous forme de chaîne de caractères
# svg_content = """<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200" version="1.1">
#     <!-- Dessiner un cercle bleu -->
#     <circle cx="100" cy="100" r="50" fill="blue" />
#     <!-- Ajouter un texte blanc -->
#     <text x="70" y="105" fill="white" font-size="20">Hello SVG!</text>
# </svg>"""

# # Écrire le contenu dans un fichier
# with open("example.svg", "w") as svg_file:
#     svg_file.write(svg_content)

# print("Image SVG créée : 'example.svg'")


svg_balise_ouvrante='<svg xmlns="http://www.w3.org/2000/svg" version="1.1" '
svg_width_value = "300"
svg_width_content = "width=\"" + svg_width_value + "\" "
svg_height_value = "300"
svg_height_content = "height=\"" + svg_height_value + "\" "
svg_balise_ouvranteTag = "> "
svg_balise_fermante=' </svg>'

test_svg_ligne = '<circle cx="100" cy="100" r="50" fill="blue" />'
test_svg_ligne2 = '<circle cx="50" cy="50" r="30" fill="red" />'
svg_newLine = "\n"

full_baliseOuvrante = svg_balise_ouvrante + svg_width_content + svg_height_content + svg_balise_ouvranteTag 

svg_contenent = full_baliseOuvrante + test_svg_ligne + test_svg_ligne2 + svg_balise_fermante

all_svg_ligne =""
for i in range(5):
    all_svg_ligne = all_svg_ligne + test_svg_ligne

print(svg_contenent)


# Écrire le contenu dans un fichier
with open("example1.svg", "w") as svg_file:
    svg_file.write(svg_contenent)
    

print("Image SVG créée : 'example1.svg'")
   