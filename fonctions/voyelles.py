
# Une fonction pour calculer le nombre de voyelles dans un mot
# definir une fonction get_vowels_numbers(mot)
# creer un compteur de voyelles
# pour chaque lettre du mot vous verifiez s'il s'agit d'une voyelle
# si c'est le cas, on ajoute un au compteur
# a la fin de la fonction, on renvoit le compteur


word = input("Entrez un mot de votre choix: ")

def get_vowels_numbers(word):
    cpt = 0
    vowels = ['a','e','i','o','u','y']
    
    for letter in word:
        if letter.lower() in vowels:
            cpt += 1
    return cpt

if get_vowels_numbers(word) == 1: 
    print("Le mot "+str(word)+" contient "+str(get_vowels_numbers(word))+" voyelle")
elif get_vowels_numbers(word) == 0:
    print("Le mot "+str(word)+" contient aucune voyelle")
else:
    print("Le mot "+str(word)+" contient "+str(get_vowels_numbers(word))+" voyelles") 