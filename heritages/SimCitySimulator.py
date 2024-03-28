
# Simulateur de ville
# Créer 3 classes: Immeuble, Supermarché et Banque
# Superclasse Batiment
# 4 immeubles, 2 supermarché et 1 banque
class Batiment:
    
    def __init__(self,floor,price,owner,humans):
        self.floor = floor
        self.price = price 
        self.owner = owner
        self.humans = humans
        
    def get_floor(self):
        return self.floor
    
    def get_price(self):
        return self.price
    
    def get_owner(self):
        return self.owner
    
    def get_humans(self):
        return self.humans
    
    def taxe(self):
        taxe = self.price * 1.25
        


class Immeuble(Batiment):
    
    def __init__(self,floor,price,owner,humans):
        
        super(). __init__(floor,price,owner,humans)
        self.flat = 10
    
    def taxe(self):
        taxe = (self.price * 1.25)+2000
        taxe -= self.price
        super().taxe()
        print("Toc, toc, toc, c'est les impots ! Taxe spécifique pour les immeubles :", taxe, "$")
    
    
       
class Supermarket(Batiment):
    
    def __init__(self,floor,price,owner,humans):
        
        super(). __init__(floor,price,owner,humans)
        self.flat = 10
    
    def taxe(self):
        taxe = (self.price * 1.25)+50000
        taxe -= self.price
        super().taxe()
        print("Toc, toc, toc, c'est les impots ! Taxe spécifique pour les supermarchés :", taxe, "$")
        
        
class Bank(Batiment):
    
    def __init__(self,floor,price,owner,humans):
        
        super(). __init__(floor,price,owner,humans)
        self.flat = 10
    
    def taxe(self):
        taxe = (self.price * 1.25)+800000
        taxe -= self.price
        super().taxe()
        print("Toc, toc, toc, c'est les impots ! Taxe spécifique pour les banques :", taxe, "$")
    

immeuble1 = Immeuble(5,500000,'Jean',75)
immeuble2 = Immeuble(7,600000,'Jon',80)
immeuble3 = Immeuble(9,850000,'Jack',120)
immeuble4 = Immeuble(4,300000,'Jade',55)
supermarket1 = Supermarket(2,500000,'Ledl',60)
supermarket2 = Supermarket(1,650000,'Carrefeur',70)
bank = Bank(1,2500000000,'Belfios',35)

print("l'immeuble 1 appartient à",immeuble1.get_owner(),". Son prix est de",int(immeuble1.get_price()),"$ .",immeuble1.get_humans(),"personnes vivent dedans.")

immeuble1.taxe() 

print("\nl'immeuble 2 appartient à",immeuble2.get_owner(),". Son prix est de",int(immeuble2.get_price()),"$ .",immeuble2.get_humans(),"personnes vivent dedans.")

immeuble2.taxe() 

print("\nl'immeuble 3 appartient à",immeuble3.get_owner(),". Son prix est de",int(immeuble3.get_price()),"$ .",immeuble3.get_humans(),"personnes vivent dedans.")

immeuble3.taxe() 

print("\nl'immeuble 4 appartient à",immeuble4.get_owner(),". Son prix est de",int(immeuble4.get_price()),"$ .",immeuble4.get_humans(),"personnes vivent dedans.")

immeuble4.taxe() 


print("\nle supermarché numéro 1 de la ville appartient à",supermarket1.get_owner(),". Son prix est de",int(supermarket1.get_price()),"$ .",supermarket1.get_humans(),"personnes y travaillent.")

supermarket1.taxe() 

print("\nle supermarché numéro 2 de la ville appartient à",supermarket2.get_owner(),". Son prix est de",int(supermarket2.get_price()),"$ .",supermarket2.get_humans(),"personnes y travaillent.")

supermarket2.taxe() 

print("\nla banque numéro 1 de la ville appartient à",bank.get_owner(),". Son prix est de",int(bank.get_price()),"$ .",bank.get_humans(),"personnes y travaillent.")

bank.taxe() 
