# Jeu du juste prix
# Chosir un nombre entre 1 et 1000
# tant que le jeu n'est pas fini
#   -> demander à l'utilisateur "entrer un prix"
#   -> si il le trouve le juste prix "c'est gagné !"
#   -> sinon on affiche "c'est moins" ou "c'est plus"

from random import shuffle

array = [100,240,760,965,234,312,651,912,289,121,682,713]

shuffle(array)

price = array[0]

print('LE JEU DU JUSTE PRIX !')
cpt = 0

while True:
    choice = int(input('Choisir un nombre entre 1 et 1000: '))
    cpt+=1
    
    if choice < price:
        print("C'est plus")
    elif choice > price:
        print("C'est moins")
    else:
        print("Bravo vous avez gagné, vous l'avez trouvé en {} tentatives".format(cpt))
        break