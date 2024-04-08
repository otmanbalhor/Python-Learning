
def getAge():
    while True:
        try:
            age = int(input('Quel age avez-vous ? '))
            if age < 0:
                print("L'age ne peut pas être négatif. Veuillez saisir un age valide.")
                continue
            return age
        except ValueError:
            print('Veuillez saisir un nombre entier pour votre age.')

def minorOrAdult(age):
    if age < 18:
        return "mineur"
    else:
        return "majeur"
    
age = getAge()
print("Vous êtes",minorOrAdult(age)) 

