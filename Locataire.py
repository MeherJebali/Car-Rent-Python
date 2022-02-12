import csv
from tabulate import tabulate
import operator
class Locataire:
    listeLocataires = []
    
    def __init__(self):
        listeLocataires = self.ChargerLocataires(self)

    #ChargerLocataires : Cette méthode sert à charger les données (les locataires) depuis le fichier CSV lors de l'intialisation du programme
    #et les charger dans une liste afin de minimiser la consultationdu fichier directement , dans le cadre de l'amélioration
    def ChargerLocataires(self):
        with open('Datas\Locataire.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.listeLocataires.append(row)
        file.close()
        return self.listeLocataires

    #AfficherLocataires : Sert à afficher la liste des locataires chargés dans le cache qui ont été chargées lors de démarrage de programme
    def AfficherLocataires(self):
        head = self.listeLocataires[0]
        print(tabulate(self.listeLocataires[1:len(self.listeLocataires)], headers=head, tablefmt='orgtbl'))

    #AfficherLocatairesTries : Sert à afficher la liste des locataires triés
    def AfficherLocatairesTries(self):
        liste = []
        head = self.listeLocataires[0]
        liste=self.listeLocataires[1:len(self.listeLocataires)]
        numChoix = int(input("Sur quel champ vous voulez faire le trie :\n 1 - Nom :\n 2 - Prenom\n 3 - Adresse\n votre choix SVP : "))
        if numChoix == 1:
            liste.sort(key=operator.itemgetter(1))
        elif numChoix == 2:
            liste.sort(key=operator.itemgetter(2))
        elif numChoix == 3:
            liste.sort(key=operator.itemgetter(3))
        else:
            print("Aucune choix valide choisie , nous allons utiliser le tri par défaut  ")
        print(tabulate(liste, headers=head, tablefmt='orgtbl'))

    #listeIDLocataires : Cette méthode charge la liste des Id des locataires , ça sera utilise lors de l'insertion, ajout (pour éviter les doublons),suppresion
    def listeIDLocataires(self):
        listelocID = []
        for v in self.listeLocataires [1:len(self.listeLocataires)]:
            listelocID.append(v[0])
        #convertir la liste des matricules en une liste des entiers pour faciliter la recherche
        listelocID = list(map(int, listelocID))
        return listelocID

    #AjouterLocataire : c'est pour ajouter un locataire
    def AjouterLocataire(self):
        CRED = '\033[91m' #couleur rouge 
        CORA='\033[33m' #couleur orange
        CEND = '\033[0m' #reset couleur
        while True:
            try:
                id_loc = int(input("Merci de saisir l'identifiant du client : "))
            except:
                print(CRED+"l'identifiant du client doit être de format entier"+CEND)
            else:
                if id_loc in self.listeIDLocataires(self): #pour vérifier si le matricule existe déjà
                    print(CORA+"Cet identifiant existe déjà dans la base de données , merci de saisir un autre "+CEND)
                else:
                    break
        nom = str(input("Merci de saisir le nom du locataire : "))
        while nom.isspace() or nom=='':
            nom = str(input("Merci de saisir le nom du locataire (Ne peut pas être vide) : "))
        prenom = str(input("Merci de saisir le prénom du locataire : "))
        while prenom.isspace() or prenom=='':
            prenom = str(input("Merci de saisir le prénom du locataire (Ne peut pas être vide) : "))
        adresse = str(input("Merci de saisir l'adresse du locataire : "))
        while adresse.isspace() or adresse=='':
            adresse = str(input("Merci de saisir l'adresse du locataire (Ne peut pas être vide) : "))
        NewLocataire = [id_loc,nom,prenom,adresse] #création d'une liste à partir des données saisiees
        self.listeLocataires.append(NewLocataire) # ajout de cette à la liste des voitures chargés dans le cache
        self.EnregistrerDonnees(self)

    #VerifIDLocataire : pour éviter les redondance du code et dans le cadre d'amélioration , j'ai sortie la méthode de saisie et recherche de matricule dans une méthode séparée   
    def VerifIDLocataire(self):
        CRED = '\033[91m' #couleur rouge 
        CORA='\033[33m' #couleur orange
        CEND = '\033[0m' #reset couleur
        while True:
            try:
                id_loc = int(input("Merci de saisir l'identifiant de locataire : "))
            except:
                
                print(CRED+"l'identifiant doit être de format entier"+CEND)
            else:
                if id_loc not in self.listeIDLocataires(self): #pour vérifier si le matricule existe déjà
                    print(CORA+"Cet identifiant n'existe pas dans la base de données , merci de saisir un autre "+CEND)
                else:
                    break
        return id_loc
    
    def SupprimerLocatire(self):
        id = self.VerifIDLocataire(self)
        confirm = None
        while (confirm not in ['O','o','N','n']):
            try:
                confirm = input(str("Voulez-vous vraiment supprimer ce client (O/N) ? : "))
            except:
                print("Merci de Saisir O pour OUI ou N pour NON")
            if confirm == 'O' or confirm == 'o':
                self.listeLocataires.remove(self.listeLocataires[self.listeIDLocataires(self).index(id)+1]) #on ajoute +1 pour prendre en considération le header du CSV
                self.EnregistrerDonnees(self)
            elif confirm == 'N' or confirm == 'n':
                break


    def ModifierLocataire(self):
        CRED = '\033[91m' #couleur rouge 
        CEND = '\033[0m' #reset couleur
        id = self.VerifIDLocataire(self)
        loc = self.listeLocataires[self.listeIDLocataires(self).index(id)+1]
        newID = loc[0] # on change pas l'identifiant du client
        newnom = str(input("Merci de saisir le nouveau nom ("+loc[1]+") : ") or loc[1])
        if(newnom=='' or newnom.isspace()):
            newnom=loc[1]
        newprenom = str(input("Merci de saisir le nouveau prénom ("+loc[2]+") : ") or loc[2])
        if(newprenom=='' or newprenom.isspace()):
            newprenom=loc[2]
        newadress = str(input("Merci de saisir l'adresse de client ("+loc[3]+") : ") or loc[3])
        if(newadress=='' or newadress.isspace()):
            newadress=loc[3]
        newLocat = [newID,newnom,newprenom,newadress]
        print("les anciennes valeur : "+str(loc))
        print("les nouvelles valeurs : "+str(newLocat))
        confirm = None
        while (confirm not in ['O','o','N','n']):
            try:
                confirm = input(str("Voulez-vous vraiment enregistrer ces modification (O/N) ? : "))
            except:
                print("Merci de Saisir O pour OUI ou N pour NON")
            if confirm == 'O' or confirm == 'o':
                self.listeLocataires[self.listeIDLocataires(self).index(id)+1] = newLocat
                self.EnregistrerDonnees(self)
            elif confirm == 'N' or confirm == 'n':
                break            
    
    #RechercherParID : cette méthode cherche un locataire selon son ID
    def RechercherParID(self):
        CRED = '\033[91m' #couleur rouge
        CGRE = '\033[92m' #reset couleur
        CEND = '\033[0m' #reset couleur
        id = self.VerifIDLocataire(self)
        loc = self.listeLocataires[self.listeIDLocataires(self).index(id)+1]
        print(CGRE+str(loc)+CEND)
    #RechercherParNon : cette méthode cherche un locataire selon son nom
    def RechercherParNon(self):
        CGRE = '\033[92m' #reset couleur
        CEND = '\033[0m' #reset couleur
        nom = str(input("Merci de saisir le nom du locataire à chercher : "))
        while nom.isspace() or nom=='':
            nom = str(input("Merci de saisir le nom du locataire (Ne peut pas être vide) : "))
        for l in self.listeLocataires[1:len(self.listeLocataires)]:
            if((l[1]).lower()==nom.lower()):
                print(CGRE+str(l)+CEND)

    #EnregistrerDonnees:cette méthode enregistre les modifications effectuées sur la liste listeLocataires dans le fichier
    def EnregistrerDonnees(self):
        with open('Datas\Locataire.csv', 'w',newline='') as file:
            wr = csv.writer(file)
            wr.writerows(self.listeLocataires)
        file.close()
        self.AfficherLocataires(self)