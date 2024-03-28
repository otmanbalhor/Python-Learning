

eleves = {
    'Paul':{'note':12,'appreciation': 'Peu mieux faire'},
    'Camille':{'note':8,'appreciation': 'Catastrophique'},
    'Théo':{'note':17,'appreciation': 'Excellent'}
}


# ajouter un.e eleve
eleves['Lea'] = {
    
    'note':10,
    'appreciation':'Peu mieux faire'
}

for eleve in eleves:
    print(eleve, eleves[eleve]['note'],eleves[eleve]['appreciation'])
    
    
eleves['Camille']['note'] = 18
eleves['Camille']['appreciation'] = 'Excellent trimestre !'


for eleve in eleves:
    print(eleve, eleves[eleve]['note'],eleves[eleve]['appreciation'])

del eleves['Camille']

for eleve in eleves:
    print(eleve, eleves[eleve]['note'],eleves[eleve]['appreciation'])
    
if 'Camille' in eleves.keys():
    print('Camille est dans la classe')
else:
    print("Camille n'est pas présente")
