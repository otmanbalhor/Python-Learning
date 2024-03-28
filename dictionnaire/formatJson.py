import json

with open('classe.json','r') as file:
    eleves = json.load(file)


for eleve in eleves:
    print(eleve, eleves[eleve]['note'],eleves[eleve]['appreciation'])
    
with open('classe.json','w+') as file:
    json.dump(eleves, file)