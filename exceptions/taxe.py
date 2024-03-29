
while True:
    try:
        prixHT = int(input("Entrez le prix hors taxe "))
        prixTTC = prixHT + prixHT * 0.2
        print(prixTTC)
        break
    except ValueError:
        print('Attention tu dois rentrer un nombre')    