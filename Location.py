import csv
from tabulate import tabulate
import Voiture as voit2
import Locataire as loc2
v = voit2.Voiture
l = loc2.Locataire
class Location:
    listelocation = []
    def __init__(self):
        listelocation = self.Chargerlocation(self)

    def Chargerlocation(self):
        with open('Datas\location.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.listelocation.append(row)
        file.close()
        return self.listelocation

    def louer(self):
        if(len(v.StatutVoitures(v,"1"))>0):
            head = v.listeVoiture[0]
            print("Ci-dessous les voitures disponibles , merci de choisir une voiture : ")
            print(tabulate(v.StatutVoitures(v,"1"), headers=head, tablefmt='orgtbl'))
            listIDDispo = []
            for vo in v.StatutVoitures(v,"1"):
                listIDDispo.append(vo[0])
            listIDDispo = list(map(int, listIDDispo))
            while True:
                try:
                    num_imma = int(input("Merci de saisir le matricule de la voiture : "))
                except:
                    
                    print("le matricule de la voiture doit être de format entier")
                else:
                    if num_imma not in listIDDispo: #pour vérifier si le matricule existe déjà
                        print("Ce matricule n'existe pas dans la base de données , merci de saisir un autre ")
                    else:
                        break
            l.AfficherLocataires(l)
            while True:
                try:
                    num_client = int(input("Merci de saisir le numéro de client : "))
                except:
                    
                    print("le code client doit être de format entier")
                else:
                    if num_client not in l.listeIDLocataires(l): #pour vérifier si le matricule existe déjà
                        print("Ce client n'existe pas dans la base de données , merci de saisir un autre ")
                    else:
                        break
            while True:
                try:
                    nbre_jour = int(input("Merci de saisir le nombre de jours: "))
                except:
                    print("le nombre de jour doit être de format entier")
                else:
                    if nbre_jour<0:
                        print("le nombre de jours ne peut pas être négatif")
                    else:
                        break
            confirm = None
            while (confirm not in ['O','o','N','n']):
                try:
                    confirm = input(str("Voulez-vous vraiment enregistrer la location de "+ str(nbre_jour) +" jours de la voiture " + v.StatutVoitures(v,"1")[listIDDispo.index(num_imma)][1] + " " + v.StatutVoitures(v,"1")[listIDDispo.index(num_imma)][2] + " pour le client " + l.listeLocataires[l.listeIDLocataires(l).index(num_client)+1][1] + " " + l.listeLocataires[l.listeIDLocataires(l).index(num_client)+1][2])+" (O/N) ?")
                except:
                    print("Merci de Saisir O pour OUI ou N pour NON")
                if confirm == 'O' or confirm == 'o':
                    nvlelocation = [num_imma,num_client,nbre_jour]
                    self.listelocation.append(nvlelocation)
                    self.EnregistrerDonnees(self)
                    v.changerStaut(v,num_imma)
                    self.EnregistrerDonneesHisto(self)
                elif confirm == 'N' or confirm == 'n':
                    break
        else:
            print("Désolé , il n y a plus des voitures disponibles")

    #rendreVoiture : pour maj à jour le statut de la voiture quand elle est retounée
    def RendreVoiture(self):
        if(len(v.StatutVoitures(v,"1"))>0):
            head = v.listeVoiture[0]
            print("Ci-dessous les voitures louées , merci de choisir une voiture : ")
            print(tabulate(v.StatutVoitures(v,"0"), headers=head, tablefmt='orgtbl'))
            listIDDispo = []
            for vo in v.StatutVoitures(v,"0"):
                listIDDispo.append(vo[0])
            listIDDispo = list(map(int, listIDDispo))
            while True:
                try:
                    num_imma = int(input("Merci de saisir le matricule de la voiture : "))
                except:
                    
                    print("le matricule de la voiture doit être de format entier")
                else:
                    if num_imma not in listIDDispo: #pour vérifier si le matricule existe déjà
                        print("Ce matricule n'existe pas dans la base de données , merci de saisir un autre ")
                    else:
                        break
            listeIDVoiturelues = []
            for ll in self.listelocation[1:len(self.listelocation)]:
                listeIDVoiturelues.append(ll[0])
            listeIDVoitureloues = list(map(int, listeIDVoiturelues))
            confirm = None
            while (confirm not in ['O','o','N','n']):
                try:
                    confirm = input(str("Voulez-vous vraiment retourner la voiture de " + v.StatutVoitures(v,"0")[listIDDispo.index(num_imma)][1] + " " + v.StatutVoitures(v,"0")[listIDDispo.index(num_imma)][2] + " dans le garage (O/N) ?"))
                except:
                    print("Merci de Saisir O pour OUI ou N pour NON")
                if confirm == 'O' or confirm == 'o':
                    self.listelocation.remove(self.listelocation[(listeIDVoitureloues.index(num_imma))+1])
                    v.changerStaut(v,num_imma)
                    self.EnregistrerDonnees(self)
                elif confirm == 'N' or confirm == 'n':
                    break

        else:
            print("Toutes les voitures sont dans les garages")

    #Statistique : cette méthode fait un résumé de l'état du parc
    def Statistique(self):
        head = v.listeVoiture[0]
        print("Le nombre total des voitures est : "+str(v.NbreTotalVoiture(v)))
        print("Le nombre des voitures louées : "+str(len(v.StatutVoitures(v,"0"))))
        if(len(v.StatutVoitures(v,"0"))>0):
            print("et ci-dessous les détails : ")
            print(tabulate(v.StatutVoitures(v,"0"), headers=head, tablefmt='orgtbl'))
        print("Le nombre des voitures disponibles : "+str(len(v.StatutVoitures(v,"1"))))
        if(len(v.StatutVoitures(v,"1"))>0):
            print("et ci-dessous les détails :")
            print(tabulate(v.StatutVoitures(v,"1"), headers=head, tablefmt='orgtbl'))
        print("La moyenne de kilométrage est : "+str(v.KilometrageMoyen(v)))

    #EnregistrerDonnees:cette méthode enregistre les modifications effectuées sur la liste listeVoiture dans le fichier
    def EnregistrerDonnees(self):
        with open('Datas\location.csv', 'w',newline='') as file:
            wr = csv.writer(file)
            wr.writerows(self.listelocation)
        file.close()

    #EnregistrerDonnees:cette méthode enregistre les modifications effectuées sur la liste listeLocataires dans le fichier
    def EnregistrerDonneesHisto(self):
        with open('Datas\Historique.csv', 'w',newline='') as file:
            wr = csv.writer(file)
            wr.writerows(self.listelocation)
        file.close()