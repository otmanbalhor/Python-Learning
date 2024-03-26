from random import shuffle

# Générateur de phrases

words = input('Veuillez entrez les mots qui vous passent par la tête en respectant la forme suivante (mot1/mot2/mot3/mot4 etc)')

array = words.split('/')

shuffle(array)

print(array)

length = len(array)

if length < 10 :
    print(array[0],array[1])
else:
    print(array[length - 3],array[length - 2],array[length - 1])

