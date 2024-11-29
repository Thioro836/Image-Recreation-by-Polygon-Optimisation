from PIL import Image, ImageDraw

# Exemple de génotype avec différents types de formes
genotype = [
    {"shape": "circle", "x": 50, "y": 70, "radius": 30, "color": (255, 0, 0)},  # Cercle rouge
    {"shape": "square", "x": 120, "y": 100, "size": 40, "color": (0, 255, 0)},  # Carré vert
    {"shape": "rectangle", "x": 200, "y": 150, "width": 60, "height": 30, "color": (0, 0, 255)},  # Rectangle bleu
    {"shape": "polygon", "points": [(300, 50), (350, 70), (330, 120), (290, 100)], "color": (255, 255, 0)},  # Polygone jaune
]

# Créer une image vide (par exemple, 400x400 pixels)
image_width = 400
image_height = 400
image = Image.new("RGB", (image_width, image_height), color=(255, 255, 255))  # Fond blanc

# Créer un objet ImageDraw pour dessiner sur l'image
draw = ImageDraw.Draw(image)

# Dessiner les formes à partir du génotype
for shape in genotype:
    if shape["shape"] == "circle":
        # Dessiner un cercle
        x = shape["x"]
        y = shape["y"]
        radius = shape["radius"]
        color = shape["color"]
        upper_left = (x - radius, y - radius)
        bottom_right = (x + radius, y + radius)
        draw.ellipse([upper_left, bottom_right], fill=color)
    
    elif shape["shape"] == "square":
        # Dessiner un carré
        x = shape["x"]
        y = shape["y"]
        size = shape["size"]
        color = shape["color"]
        upper_left = (x, y)
        bottom_right = (x + size, y + size)
        draw.rectangle([upper_left, bottom_right], fill=color)
    
    elif shape["shape"] == "rectangle":
        # Dessiner un rectangle
        x = shape["x"]
        y = shape["y"]
        width = shape["width"]
        height = shape["height"]
        color = shape["color"]
        upper_left = (x, y)
        bottom_right = (x + width, y + height)
        draw.rectangle([upper_left, bottom_right], fill=color)
    
    elif shape["shape"] == "polygon":
        # Dessiner un polygone
        points = shape["points"]
        color = shape["color"]
        draw.polygon(points, fill=color)

# Sauvegarder l'image générée en PNG
image.save("output.png")

# Optionnel : Afficher l'image (si vous utilisez un environnement local, comme un IDE)
image.show()

print("Image PNG générée : output.png")
