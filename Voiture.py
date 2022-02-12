import csv
from tabulate import tabulate
class Voiture:
    listeVoiture = []
    
    def __init__(self):
        listeVoiture = self.ChargerVoitures(self)

    #ChargerVoitures : Cette méthode sert à charger les données (les voitures) depuis le fichier CSV lors de l'intialisation du programme
    #et les charger dans une liste afin de minimiser la consultationdu fichier directement , dans le cadre de l'amélioration
    def ChargerVoitures(self):
        with open('Datas\Voiture.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.listeVoiture.append(row)
        file.close()
        return self.listeVoiture

    #AfficherVoiture : Sert à afficher la liste des voitures chargés dans le cache qui ont été chargées lors de démarrage de programme
    def AfficherVoiture(self):
        head = self.listeVoiture[0]
        print(tabulate(self.listeVoiture[1:len(self.listeVoiture)], headers=head, tablefmt='orgtbl'))
        

    #ListeMatricules : Cette méthode charge la liste des matricules des voitures , ça sera utilise lors de l'insertion, ajout (pour éviter les doublons),suppresion
    def ListeMatricules(self):
        matriculesVoitures = []
        for v in self.listeVoiture[1:len(self.listeVoiture)]:
            matriculesVoitures.append(v[0])
        #convertir la liste des matricules en une liste des entiers pour faciliter la recherche
        matriculesVoitures = list(map(int, matriculesVoitures))
        return matriculesVoitures

    #AjouterVoiture : c'est pour ajouter une voiture
    def AjouterVoiture(self):
        CRED = '\033[91m' #couleur rouge 
        CORA='\033[33m' #couleur orange
        CEND = '\033[0m' #reset couleur
        while True:
            try:
                num_imma = int(input("Merci de saisir le matricule de la voiture : "))
            except:
                
                print(CRED+"le matricule de la voiture doit être de format entier"+CEND)
            else:
                if num_imma in self.ListeMatricules(self): #pour vérifier si le matricule existe déjà
                    print(CORA+"Ce matricule existe déjà dans la base de données , merci de saisir un autre "+CEND)
                else:
                    break
        marque = str(input("Merci de saisir la marque de la voiture : "))
        while marque.isspace() or marque=='':
            marque = str(input("Merci de saisir la marque de la voiture (Ne peut pas être vide) : "))
        modele = str(input("Merci de saisir le modèle de la voiture : "))
        while modele.isspace() or modele=='':
            modele = str(input("Merci de saisir le modèle de la voiture (Ne peut pas être vide) : "))
        while True:
            try:
                kilometrage = int(input("Merci de saisir le kilométrage de la voiture : "))
            except:
                print(CRED+"le kilométrage de la voiture doit être de format entier"+CEND)
            else:
                break
        etat = 1 # par défaut on considère toujours que la voiture est disponible donc on affecte la valeur 1
        while True:
            try:
                prix_location = float(input("Merci de saisir le prix de location de la voiture : "))
            except:
                print(CRED+"le prix de location de la voiture doit être de format réél"+CEND)
            else:
                break
        NewVoiture = [num_imma,marque,modele,kilometrage,etat,prix_location] #création d'une liste à partir des données saisiees
        self.listeVoiture.append(NewVoiture) # ajout de cette à la liste des voitures chargés dans le cache
        self.EnregistrerDonnees(self)

    def SupprimerVoiture(self):
        mat = self.VerifMatricule(self)
        confirm = None
        while (confirm not in ['O','o','N','n']):
            try:
                confirm = input(str("Voulez-vous vraiment supprimer cette voiture (O/N) ? : "))
            except:
                print("Merci de Saisir O pour OUI ou N pour NON")
            if confirm == 'O' or confirm == 'o':
                self.listeVoiture.remove(self.listeVoiture[self.ListeMatricules(self).index(mat)+1]) #on ajoute +1 pour prendre en considération le header du CSV
                self.EnregistrerDonnees(self)
            elif confirm == 'N' or confirm == 'n':
                break
        
    def MAJVoiture(self):
        CRED = '\033[91m' #couleur rouge 
        CEND = '\033[0m' #reset couleur
        self.AfficherVoiture(self)
        mat = self.VerifMatricule(self)
        voit = self.listeVoiture[self.ListeMatricules(self).index(mat)+1]
        newmatricule = voit[0] # on change pas le matricule de la voiture
        newmarque = str(input("Merci de saisir la nouvelle marque ("+voit[1]+") : ") or voit[1])
        if(newmarque=='' or newmarque.isspace()):
            newmarque=voit[1]
        newmodele = str(input("Merci de saisir le nouveau modèle ("+voit[2]+") : ") or voit[2])
        if(newmodele=='' or newmodele.isspace()):
            newmodele=voit[2]
        while True:
            try:
                newkilometrage = int(input("Merci de saisir le nouveau kilométrage("+voit[3]+") : ") or voit[3])
            except:
                print(CRED+"le kilométrage de la voiture doit être de format entier"+CEND)
            else:
                break
        newetat=voit[4]
        while True:
            try:
                newprix_location = float(input("Merci de saisir le nouveau prix de location("+voit[5]+") : ") or voit[5])
            except:
                print(CRED+"le prix de location de la voiture doit être de format réél"+CEND)
            else:
                break
        
        NewVoiture = [newmatricule,newmarque,newmodele,newkilometrage,newetat,newprix_location]
        print("les anciennes valeur : "+str(voit))
        print("les nouvelles valeurs : "+str(NewVoiture))
        confirm = None
        while (confirm not in ['O','o','N','n']):
            try:
                confirm = input(str("Voulez-vous vraiment enregistrer ces modification (O/N) ? : "))
            except:
                print("Merci de Saisir O pour OUI ou N pour NON")
            if confirm == 'O' or confirm == 'o':
                self.listeVoiture[self.ListeMatricules(self).index(mat)+1] = NewVoiture
                self.EnregistrerDonnees(self)
            elif confirm == 'N' or confirm == 'n':
                break

    # VerifDispoVoiture = pour vérifier la disponiblité d'une voiture
    def VerifDispoVoiture(self):
        CGRE = '\033[92m' #reset couleur
        CEND = '\033[0m' #reset couleur
        mat = self.VerifMatricule(self)
        voit = self.listeVoiture[self.ListeMatricules(self).index(mat)+1]
        if(voit[4]=='1'):
            print(CGRE+"La voiture "+voit[1] +" "+voit[2]+" de matricule "+voit[0]+" est actuellement disponible"+CEND)
        elif(voit[4]=='0'):
            print(CGRE+"La voiture "+voit[1] +" "+voit[2]+" de matricule "+voit[0]+" est actuellement indisponible"+CEND)

    #VoituresDispo : retourne la liste des voitures disponibles, prend en paramètres l'état lors de l'appel 1=dispo , 0=louée
    def StatutVoitures(self,etat):
        voituresstatut = []
        for v in self.listeVoiture[1:len(self.listeVoiture)]: # on commence par 1 pour ignorer la ligne de header de CSV
            if(v[4]==etat):
                voituresstatut.append(v)
        return voituresstatut


    #def NbreTotalVoiture:une fonction qui retourne le nombre totla des voitures
    def NbreTotalVoiture(self):
        return len(self.listeVoiture)-1 #-1 pour décompter le header

    #KilometrageMoyen: retourne la moyenne des kilométrages des toutes les voitures
    def KilometrageMoyen(self):
        somme=0
        for v in self.listeVoiture[1:len(self.listeVoiture)]:
            somme=somme+int(v[3])

        return somme/self.NbreTotalVoiture(self)

    #VerifMatricule : pour éviter les redondance du code et dans le cadre d'amélioration , j'ai sortie la méthode de saisie et recherche de matricule dans une méthode séparée   
    def VerifMatricule(self):
        CRED = '\033[91m' #couleur rouge 
        CORA='\033[33m' #couleur orange
        CEND = '\033[0m' #reset couleur
        while True:
            try:
                num_imma = int(input("Merci de saisir le matricule de la voiture : "))
            except:
                
                print(CRED+"le matricule de la voiture doit être de format entier"+CEND)
            else:
                if num_imma not in self.ListeMatricules(self): #pour vérifier si le matricule existe déjà
                    print(CORA+"Ce matricule n'existe pas dans la base de données , merci de saisir un autre "+CEND)
                else:
                    break
        return num_imma

    #changerStaut: cette méthode prend en paramètre l'id de la voiture et change le statut (louée/non louée), elle va être utilsié lors de louer et rendre une voiture
    def changerStaut(self,mat):
        voit = self.listeVoiture[self.ListeMatricules(self).index(mat)+1]
        newmatricule = voit[0]
        newmarque=voit[1]
        newmodele=voit[2]
        newkilometrage=voit[3]
        newetat=voit[4]
        if(voit[4]=="0"):
            newetat=1
        elif(voit[4]=="1"):
            newetat=0
        newprix_location=voit[5]
        NewVoiture = [newmatricule,newmarque,newmodele,newkilometrage,newetat,newprix_location]
        self.listeVoiture[self.ListeMatricules(self).index(mat)+1] = NewVoiture
        self.EnregistrerDonnees(self)

    #EnregistrerDonnees:cette méthode enregistre les modifications effectuées sur la liste listeVoiture dans le fichier
    def EnregistrerDonnees(self):
        with open('Datas\Voiture.csv', 'w',newline='') as file:
            wr = csv.writer(file)
            wr.writerows(self.listeVoiture)
        file.close()
        self.AfficherVoiture(self)
        