from PIL import Image, ImageDraw

# Exemple de génotype avec différents types de formes

def generatePng(genotype: list, output:str, width:int, height:int):

    # Créer une image vide (par exemple, 400x400 pixels)
    image_width = width
    image_height = height
    image = Image.new("RGB", (image_width, image_height), color=(255, 255, 255))  # Fond blanc

    # Créer un objet ImageDraw pour dessiner sur l'image
    draw = ImageDraw.Draw(image)
    genotype=genotype
    # Dessiner les formes à partir du génotype
    for shape in genotype:
        
        if shape["shape"] == "square":
            # Dessiner un carré
            x = shape["x"]
            y = shape["y"]
            width = shape["width"]
            height=shape["height"]
            color = shape["color"]
            upper_left = (x, y)
            bottom_right = (x + width, y + height)
            draw.rectangle([upper_left, bottom_right], fill=color)
        elif shape["shape"] == "circle":
            # Dessiner un cercle
            x = shape["x"]
            y = shape["y"]
            radius = shape["radius"]
            color = shape["color"]
            upper_left = (x - radius, y - radius)
            bottom_right = (x + radius, y + radius)
            draw.ellipse([upper_left, bottom_right], fill=color)
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

    # Sauvegarder l'image genere en PNG
    
    image.save(output.split(".")[0] + ".png")

    # Optionnel : Afficher l'image (si vous utilisez un environnement local, comme un IDE)
    # image.show()

    print("Image PNG generer : output.png")

