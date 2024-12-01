
import random

def mutate_genotype(genotype, mutation_rate=0.1):
    """
    Applique une mutation aléatoire sur le génotype.
    
    Arguments :
    - genotype : list, le génotype représentant les formes géométriques.
    - mutation_rate : float, probabilité qu'une mutation soit appliquée (entre 0 et 1).
    
    Retourne :
    - mutated_genotype : list, une version modifiée du génotype.
    """
    mutated_genotype = genotype.copy()
    
    for shape in mutated_genotype:
        if random.random() < mutation_rate:  # Appliquer la mutation avec une certaine probabilité
            mutation_type = random.choice(["position", "dimension", "color"])
            
            if mutation_type == "position":
                # Modifier aléatoirement la position
                shape["x"] += random.randint(-10, 10)
                shape["y"] += random.randint(-10, 10)
            
            elif mutation_type == "dimension":
                # Modifier aléatoirement les dimensions (si applicable)
                if "width" in shape:
                    shape["width"] = max(1, shape["width"] + random.randint(-15, 15))  # Min 1 pour éviter 0
                if "height" in shape:
                    shape["height"] = max(1, shape["height"] + random.randint(-15, 15))
                if "radius" in shape:
                    shape["radius"] = max(1, shape["radius"] + random.randint(-15, 15))
            
            elif mutation_type == "color":
                # Modifier aléatoirement la couleur
                shape["color"] = (
                    min(255, max(0, shape["color"][0] + random.randint(-120, 120))),
                    min(255, max(0, shape["color"][1] + random.randint(-120, 120))),
                    min(255, max(0, shape["color"][2] + random.randint(-120, 120))),
                )
    
    return mutated_genotype
