

wallet = 8000
computer_price = 1200

if computer_price <= wallet:
    print("L'achat est possible")
    wallet-=computer_price  
else:
    print("Non, l'achat est impossible, vous n'avez que {}$".format(wallet))
    

print("Your wallet: "+str(wallet)+"$")