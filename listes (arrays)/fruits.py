
fruits = ["Pomme", "Fraise", "Banane"]

print(fruits)

# modification de pomme par orange

# fruits[0] = "Orange"

#injecter une valeur en plus dans mon array

fruits.insert(2,'Poire')

#modifie plusieurs valeurs à la fois

fruits[2:4] = ['Framboise','Mirtille']

print(fruits)

# On imagine qu'un fruit "Grenade" s'ajoute

fruits.append("Grenade")

print(fruits)

# Pour ajouter plusieurs elements à notre tableau

fruits.extend(["Cerise","Abricot"])

print(fruits)

# On a plus de Fraise donc on doit le virer du tableau

fruits.pop(1)

print(fruits)

# vider notre liste

fruits.clear()

print(fruits)

