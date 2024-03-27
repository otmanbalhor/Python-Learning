



def multiply():
    result = 5 * 5
    return result

print("Le resultat du calcul est",multiply())

def sum(n):
    return 5 + n

print("Le resultat du calcul est",sum(5))
print("Le resultat du calcul est",sum(9))

# Creer une fonction max() qui va renvoyer le resultat le plus haut parmis 2 valeurs

def max(a,b):
    if a > b:
        return a
    elif a == b:
        result = print("Les 2 chiffres que vous avez choisis sont égaux")
        return result
    else:
        return b
    
    
print("Le chiffre le plus grand est",max(10,10))
    