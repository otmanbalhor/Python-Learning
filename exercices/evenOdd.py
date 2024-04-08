
nb = int(input('Tapez un nombre de votre choix:'))


def oddOrEven(nb):
    nb %= 2
    
    if nb == 1:
        
        impair = "impair"
        return impair
    else:
        pair = "pair"
        return pair
    
    
print('Le nombre que vous avez tapé est',oddOrEven(nb))
    