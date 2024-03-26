
def main():
    basket = 50
    valUser = int(input("Entrez la valeur de votre porte monnaie"))
    if valUser < 50 :
        print("Vous etes pauvre, allez bosser")
    else:
        valUser -= basket  
        print("Voici la valeur de votre porte monnaie apres l'achat : "+str(valUser)+"$")
    
    
if __name__ == '__main__':
    main() 
    
    