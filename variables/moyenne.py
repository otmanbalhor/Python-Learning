
def main():
    note1 = int(input('Entrez la premiere note'))
    note2 = int(input('Entrez la seconde note'))
    note3 = int(input('Entrez la troisieme note'))
    result = (note1+note2+note3) / 3
    
    
    print("Voici la moyenne: "+str(result))
    
    
    
if __name__ == '__main__':
    main()