
import random
from image_recreation.utils.svg_square_tag import svg_square_tag
from image_recreation.utils.svg_tags.svg_circle_tag import svg_circle_tag
from image_recreation.utils.svg_tags.svg_rect_tag import svg_rect_tag
from image_recreation.utils.svg_tags.svg_ellipse_tag import svg_ellipse_tag
from image_recreation.utils.svg_tags.svg_polygon_tag import svg_polygon_tag
#recupérer les différentes formes du genotype
def getSvgLine(shape:str, x:int, y:int, red:int, green:int, blue:int):
    if(shape=="rect"):
        return svg_rect_tag(x=x, y=y, width=40, height=30,red=red, green=green, blue=blue)
    elif(shape=="circle"):
        return svg_circle_tag(cx=x, cy=y, rayon=30,red=red, green=green, blue=blue)
    elif(shape=="ellipse"):
        return svg_ellipse_tag(cx=x, cy=y, rx=30,ry=30,red=red, green=green, blue=blue)
    elif(shape=="square"):
         return svg_square_tag(x=x, y=y, width=100,height=200,red=red, green=green, blue=blue)  
    elif(shape=="polygon"):
        points = [(x, y), (x + 30, y + 30), (x + 60, y)]
        return svg_polygon_tag(points=points, red=red, green=green, blue=blue)
    else:
        return "Invalid shape"
    

def getGenotypeLine(shape:str, x:int, y:int, red:int, green:int, blue:int):
    if(shape=="rect"):
        return {"shape": "rectangle", "x": x, "y": y, "width": 50, "height": 30, "color": (red, green, blue)} # Rectangle
    elif(shape=="circle"):
        return {"shape": "circle", "x": x, "y": y, "radius": 30, "color": (red, green, blue)}  # Cercle
    elif(shape=="ellipse"):
        return {"shape": "ellipse", "x": x, "y": y, "radius": 30, "color": (red, green, blue)}  # Cercle
    elif (shape =="square"):
        return {"shape": "square", "x": x, "y": y, "width": 30,"height":30, "color": (red, green, blue)} # Carré 
    elif (shape =="polygon"):
         points = [(x, y), (x + 30, y + 30), (x + 60, y)]
         return {"shape": "polygon", "points": points, "color": (red, green, blue)} # Polygone
    else:
         return {"error": "Shape not recognized"}
    

    
#Computing an SVG from a genotype
def generateSvg(input_image, shape: str, n:int,width:int,height:int ,output, isPng: bool = False):
    #les dimensions de l'image à générer
    image_width=500
    image_height=500
    genotype = []
    svg_openTag = f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" version="1.1">'
    svg_closeTag = "</svg>"
    svg_all_line = ""
   
    # print("taille",width,height)
    for i in range(n):
        x= random.randint(0, width-1)
        y=random.randint(0,height-1)
        
        # Obtenir la couleur du pixel correspondant dans l'image source
        #x = int(x *  width/image_width)  # Redimensionner la position pour l'image source
        #y = int(y *  height/image_height)
        # print(x,y)
        red, green, blue = input_image.getpixel((x, y))
        svg_all_line = svg_all_line + getSvgLine(shape=shape, x=x, y=y, red=red, green=green, blue=blue)
       # print(svg_all_line)
        genotype.append(getGenotypeLine(shape=shape, x=x, y=y, red=red, green=green, blue=blue))


    # # Écrire le contenu dans un fichier
    if(isPng == False):
        with open(output, "w") as svg_file:
            svg_file.write(svg_openTag + svg_all_line + svg_closeTag)
    #print(genotype)
    return genotype