class Player:
    
    def __init__(self, pseudo, health, attack):
        
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        print("Bienvenue au joueur",pseudo, "/ Points de vie:",health,"/ Attaque:",attack)
            
    def get_pseudo(self):
        return self.pseudo
    
    def get_health(self):
        return self.health
    
    def get_attack(self):
        return self.attack
    
    def damage(self, damage):
        self.health -= damage
        print("Aie... Vous venez de subir",damage,"dégats!")
    
    def attack_player(self,target_player):
        target_player.damage(self.attack)
           

class Warrior(Player):
    
    def __init__(self, pseudo, health, attack):
        
        super(). __init__(pseudo,health,attack)
        self.armor = 3
        print("Bienvenue au guerrier",pseudo, "/ Points de vie:",health,"/ Attaque:",attack)
    
    def damage(self, damage):
        
        if self.armor > 0:
            self.armor-=1
            damage = 0
            
        super().damage(damage)
        
    def blade(self):
        self.armor = 3
        print("Les points d'armure ont été rechargé")
        
    def get_armor_point(self):
        return self.armor
    
def detect_space():
    user_input = input("Appuyez sur a (joueur 1) et b (warrior) et c (joueur 2) pour réaliser une action: ")
    if user_input.lower() == 'a':
        warrior.damage(5)
        print("vie:",warrior.get_health(),"armure:",warrior.get_armor_point())
        if warrior.get_health() < 1:
            print(warrior.get_pseudo(),"est mort.",warrior2.get_pseudo(),"et",player.get_pseudo(),"ont gagné !")
        elif player.get_health() < 1 or warrior2.get_health() < 1:
            print("Un des combatants est mort.",warrior.get_pseudo(),"a gagné !")
        else:
            print("Bienvenue au joueur",player.get_pseudo(), "/ Points de vie:",player.get_health(),"/ Attaque:",player.get_attack())
            print("Bienvenue au joueur",warrior2.get_pseudo(), "/ Points de vie:",warrior2.get_health(),"/ Attaque:",warrior2.get_attack())
            print("Bienvenue au joueur",warrior.get_pseudo(), "/ Points de vie:",warrior.get_health(),"/ Attaque:",warrior.get_attack())
    elif user_input.lower() == 'b':
        player.damage(8)
        warrior2.damage(8)
        print("vie:",player.get_health(),"armure: 0")
        print("vie:",warrior2.get_health(),"armure:",warrior2.get_armor_point())
        if player.get_health() < 1 or warrior2.get_health() < 1:
            print("Un des combatants est mort.",warrior.get_pseudo(),"a gagné !")
        elif player.get_health() < 1:
            print(warrior.get_pseudo(),"est mort.",player.get_pseudo(),"a gagné !")
        else:
            print("Bienvenue au joueur",player.get_pseudo(), "/ Points de vie:",player.get_health(),"/ Attaque:",player.get_attack())
            print("Bienvenue au joueur",warrior2.get_pseudo(), "/ Points de vie:",warrior2.get_health(),"/ Attaque:",warrior2.get_attack())
            print("Bienvenue au joueur",warrior.get_pseudo(), "/ Points de vie:",warrior.get_health(),"/ Attaque:",warrior.get_attack())
    elif user_input.lower() == 'c':
        warrior.damage(5)
        print("vie:",warrior.get_health(),"armure:",warrior.get_armor_point())
        if warrior.get_health() < 1:
            print(warrior.get_pseudo(),"est mort.",warrior2.get_pseudo(),"et",player.get_pseudo(),"ont gagné !")
        elif player.get_health() < 1 or warrior2.get_health() < 1:
            print("Un des combatants est mort.",warrior.get_pseudo(),"a gagné !")
        else:
            print("Bienvenue au joueur",player.get_pseudo(), "/ Points de vie:",player.get_health(),"/ Attaque:",player.get_attack())
            print("Bienvenue au joueur",warrior2.get_pseudo(), "/ Points de vie:",warrior2.get_health(),"/ Attaque:",warrior2.get_attack())
            print("Bienvenue au joueur",warrior.get_pseudo(), "/ Points de vie:",warrior.get_health(),"/ Attaque:",warrior.get_attack())
    else: 
        print("Ereur 404, il n'est qu'une question de temps pour que votre ordinateur soit une bombe à retardement.")
        quit()
        
        

player = Player('Otman',20,5)
warrior2 = Warrior('Damien',20,5)
warrior = Warrior('Gunnar',30,8) 
player2 = Warrior('Giuseppe',100,1)
player3 = Player('Aurelien',1,39)
player4 = Warrior('Alexis',99,2)

while True:
    detect_space()
    if player.get_health() < 1 or warrior.get_health() < 1:
        break



