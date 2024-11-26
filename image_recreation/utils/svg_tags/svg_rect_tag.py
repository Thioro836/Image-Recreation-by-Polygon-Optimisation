
def svg_rect_tag(x:int, y:int, width:int, height:int, red:int, green:int, blue:int ):
    """
    arguments:
    x:int, y:int, width:int, height:int, red:int, green:int, blue:int \n
    returns: return la balise de rect svg
    """
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}"  fill="rgb({red},{green},{blue})/>'


