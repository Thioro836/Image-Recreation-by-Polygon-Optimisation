import random
from image_recreation.utils.svg_tags.svg_circle_tag import svg_circle_tag
from image_recreation.utils.svg_tags.svg_rect_tag import svg_rect_tag
from image_recreation.utils.svg_tags.svg_square_tag import svg_square_tag
def crossover_genotypes(genotype1:list, genotype2:list):
    """
    Applique un crossover entre deux génotypes pour en créer un nouveau.
    Le crossover est effectué à un seul point.
    
    Arguments :
    - genotype1 : Le premier génotype (Parent 1).
    - genotype2 : Le deuxième génotype (Parent 2).
    
    Returns :
    - child_genotype : Le génotype de l'enfant généré.
    """
    #vérifier la taille des éléments des parents
    if len(genotype1) == 0 or len(genotype2) == 0:
        raise ValueError("Les génotypes ne doivent pas être vides.")

    #on choisit un point de croisement aléatoire basé sur le plus court des deux génotypes
    crossover_point = random.randint(0, min(len(genotype1), len(genotype2)) - 1)

    # Fusionner les parties des deux parents pour créer l'enfant
    child_genotype = genotype1[:crossover_point] + genotype2[crossover_point:]

    return child_genotype
#generer des formes aleatoires
def generate_random_genotype(n, shape):
    genotype = []
    for _ in range(n):
        if shape == "circle":
            genotype.append({
                "shape": "circle",
                "x": random.randint(0, 500),
                "y": random.randint(0, 500),
                "radius": random.randint(10, 50),
                "color": (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                ),
            })
        elif shape == "square":
            size = random.randint(10, 50)
            genotype.append({
                "shape": "square",
                "x": random.randint(0, 500),
                "y": random.randint(0, 500),
                "width": size,
                "height": size,
                "color": (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                ),
            })
        elif shape == "rect":
            genotype.append({
                "shape": "rectangle",
                "x": random.randint(0, 500),
                "y": random.randint(0, 500),
                "width": random.randint(10, 50),
                "height": random.randint(10, 50),
                "color": (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                ),
            })
    return genotype

            