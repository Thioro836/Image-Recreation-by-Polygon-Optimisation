
# Exemple simplifié pour le carré
def svg_square_tag(x:int, y:int, width:int, height:int, red:int, green:int, blue:int):
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}" fill="rgb({red},{green},{blue})" />'
