import os
import sys
def verifyShape(shape: str) -> None:
    """
    description: verification du shape.\n
    Parameters: shape: string \n
    returns: None
    """
    authorizedShape = ["rect", "circle", "ellipse", "polygon","square"]

    if shape in authorizedShape:
        return None
    else:
        print("shape not autorised")
        sys.exit()
        
    
