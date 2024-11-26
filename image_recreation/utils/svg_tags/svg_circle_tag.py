
def svg_circle_tag(cx: int, cy: int, rayon: int, red: int, green: int, blue: int):
    """
    arguments:
    cx: int, cy: int, rayon: int, red: int, green: int, blue: int \n
    returns: return la balise de cercle svg
    """
    return f'<circle cx="{cx}" cy="{cy}" r="{rayon}" fill="rgb({red},{green},{blue})" />'
