import statistics
from random import shuffle

notes = [10,7,9,8,7,4,2,8]


print(notes)

result = statistics.mean(notes)

print('La moyenne de la class est de {}'.format(result))

shuffle(notes)
print(notes)


# email pseudo mdp

text = input('Entrez une chaine de la forme (email-pseudo-motdepasse)').split('-')

print(text)

print("Salut {}, ton email est {} et ton mdp est {}".format(text[1],text[0],text[2]))