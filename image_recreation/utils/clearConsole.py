import os
def clearConsole() -> None:
    """
    description: Netoye la console.\n
    Parameters: None\n
    returns: None
    """
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
