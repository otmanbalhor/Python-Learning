
age = int(input('Quel age avez-vous ? '))
price = 0

popcorn = input("Souhaitez-vous du pop corn ? (oui ou non) ")

if popcorn == 'oui' or popcorn == 'yes':
    if age < 18:
        price = 7 + 5
    else:
     price = 12 + 5
else:
    if age < 18:
        price = 7
    else:
        price = 12
        

print('Voici le prix total à payer: '+str(price)+'€')
        
        
    