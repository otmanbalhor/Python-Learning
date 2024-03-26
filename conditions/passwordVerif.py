
password = input('Entrez votre mot de passe: ')
password_length = len(password)

if password_length <= 8:
    print('Mot de passe trop court !')
elif 8 < password_length  < 12:
    print('Mot de passe moyen !')
else:
    print("mot de passe valide !")
    
    
print(password_length)