

# boucle for
for num_client in range(1,6):
    print("Vous êtes le client n°"+str(num_client))
    
# boucle foreach

emails = ['test@gmail.com','otman@gmail.com','otman@yahoo.com']

# blacklist

blacklist = ['test@yahoo.fr','test@gmail.com']

for email in emails:
    
    if email in blacklist:
        print('Email {} blacklisté'.format(email))
        continue
        
    print("email envoyé à: ",email)
    
# while : tant qu'une condition est vrai

salary = 1500

while salary < 2000:
    
    salary+=120
    
    print('Votre salaire est de ',salary, '$')
    
    
# un youtubeur "Gravinou" possède 2500 abonnés
# il gagne 10% d'audience supplementaire par mois
# on souhaite estimer, combien aura t'il d'abonnées, après 2 ans

suscribers_count = 2500

month = 0


while month <=24:
    
    suscribers_count *= 1.10
    
    print("Vous avez actuelleemnt {} abonnés !".format(int(suscribers_count)))
    
    month+=1
