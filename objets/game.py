from model.player import Player
from model.weapon import Weapon


ak47 = Weapon('AK 47', 12)
scar = Weapon('Scar',14)

player1 = Player("Otman",21,5)
player1.set_weapon(ak47)
player2 = Player("Damien",25,3)
player2.set_weapon(scar)

player1.attack_player(player2)

print(player1.get_pseudo(),"attaque",player2.get_pseudo())

if player2.get_health() < 1:
    print(player2.get_pseudo(),"est mort.",player1.get_pseudo(),"a gagné !")
elif player1.get_health() < 1:
    print(player1.get_pseudo(),"est mort.",player2.get_pseudo(),"a gagné !")
else:
    print("Bienvenue au joueur",player1.get_pseudo(), "/ Points de vie:",player1.get_health(),"/ Attaque:",player1.get_attack())
    print("Bienvenue au joueur",player2.get_pseudo(), "/ Points de vie:",player2.get_health(),"/ Attaque:",player2.get_attack())


player2.attack_player(player1)

print(player2.get_pseudo(),"attaque comme une merde",player1.get_pseudo())

if player2.get_health() < 1:
    print(player2.get_pseudo(),"est mort.",player1.get_pseudo(),"a gagné !")
elif player1.get_health() < 1:
    print(player1.get_pseudo(),"est mort.",player2.get_pseudo(),"a gagné !")
else:
    print("Bienvenue au joueur",player1.get_pseudo(), "/ Points de vie:",player1.get_health(),"/ Attaque:",player1.get_attack())
    print("Bienvenue au joueur",player2.get_pseudo(), "/ Points de vie:",player2.get_health(),"/ Attaque:",player2.get_attack())
    
player1.attack_player(player2)

print(player1.get_pseudo(),"attaque",player2.get_pseudo())

if player2.get_health() < 1:
    print(player2.get_pseudo(),"est mort.",player1.get_pseudo(),"a gagné !")
elif player1.get_health() < 1:
    print(player1.get_pseudo(),"est mort.",player2.get_pseudo(),"a gagné !")
else:
    print("Bienvenue au joueur",player1.get_pseudo(), "/ Points de vie:",player1.get_health(),"/ Attaque:",player1.get_attack())
    print("Bienvenue au joueur",player2.get_pseudo(), "/ Points de vie:",player2.get_health(),"/ Attaque:",player2.get_attack())