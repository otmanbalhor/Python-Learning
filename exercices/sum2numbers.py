
def getNumbers():
    while True:
        try:
            nb1 = int(input('Ecrivez le premier nombre de votre choix:'))
            nb2 = int(input('Ecrivez le second nombre de votre choix:'))
        
            return nb1,nb2
    
        except ValueError:
            print('Veuillez saisir 2 nombres')
       



def setSum(nb1,nb2):
    sum = nb1 + nb2
    
    return sum

nb1, nb2 = getNumbers()


print('La somme est de',setSum(nb1,nb2))