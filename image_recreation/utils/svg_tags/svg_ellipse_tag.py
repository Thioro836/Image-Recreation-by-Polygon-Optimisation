def svg_ellipse_tag(cx: int, cy: int, rx: int, ry:int, red: int, green: int, blue: int):
    """
    arguments:
    cx: int, cy: int, rayon: int, red: int, green: int, blue: int \n
    returns: return la balise de cercle svg
    """
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" transform="rotate(63,80,65)" fill="rgb({red},{green},{blue})" />'
