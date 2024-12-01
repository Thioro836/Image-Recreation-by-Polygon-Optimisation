def svg_polygon_tag(points: list, red: int, green: int, blue: int):
    """
    Arguments:
    points: liste de tuples (x, y) représentant les sommets du polygone
    rouge, vert, bleu: entiers représentant la couleur RVB du polygone
    Returns:
    string: une balise SVG <polygon>
    """
    points_str = " ".join([f"{x},{y}" for x, y in points])  # Convertir les points en une chaîne de texte
    return f'<polygon points="{points_str}" fill="rgb({red},{green},{blue})" />'
