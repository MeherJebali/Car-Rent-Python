import Voiture as voit
import Locataire as loc
import Location as loca
import os
from tabulate import tabulate
#cls pour une meilleure visibilité on fait un clear screen
def cls():
    #on importe le module os system et on teste selon le système d'exploitation si NT(Windows) on utilise la commande cls
    #sinon si un autre système telque linux , ça sera clear
    os.system('cls' if os.name=='nt' else 'clear')
v = voit.Voiture
l = loc.Locataire
lo = loca.Location
v.__init__(v)
l.__init__(l)
lo.__init__(lo)
CRED = '\033[91m' #couleur rouge 
CEND = '\033[0m' #reset couleur
cls()
choix = None
while (choix != 0):
    try:
        choix = int(input("\n\nMerci de faire votre choix - \n 01 - Affichier les voitures \n 02 - Ajouter une voiture "
              "\n 03 - Modifier une Voiture \n 04 - Supprimer une voiture \n 05 - Vérifier disponibilité d'une voiture "
              "\n 06 - Afficher les clients \n 07 - Ajouter un client \n 08 - Modifier un locataire"
              "\n 09 - Supprimer un client \n 10 - Chercher un client par son ID"
               "\n 11 - Chercher un client par son nom \n 12 - Afficher les client triés"
               "\n 13 - Louer une voiture \n 14 - Rendre une voiture \n 15 - Afficher les statistiques" 
               "\n 0 - Pour quitter \n Votre choix SVP : "))
    except:
        print(CRED+"Merci de saisir un choix entre 0 et 15"+CEND)
    if choix == 1:
        cls()
        v.AfficherVoiture(v)
    elif choix == 2:
        cls()
        v.AjouterVoiture(v)
    elif choix == 3:
        cls()
        v.MAJVoiture(v)
    elif choix == 4:
        cls()
        v.SupprimerVoiture(v)
    elif choix == 5:
        cls()
        v.VerifDispoVoiture(v)
    elif choix == 6:
        cls()
        l.AfficherLocataires(l)
    elif choix == 7:
        cls()
        l.AjouterLocataire(l)
    elif choix == 8:
        cls()
        l.ModifierLocataire(l)
    elif choix == 9:
        cls()
        l.SupprimerLocatire(l)
    elif choix == 10:
        cls()
        l.RechercherParID(l)
    elif choix == 11:
        cls()
        l.RechercherParNon(l)
    elif choix == 12:
        cls()
        l.AfficherLocatairesTries(l)
    elif choix == 13:
        cls()
        lo.louer(lo)
    elif choix == 14:
        cls()
        lo.RendreVoiture(lo)
    elif choix == 15:
        cls()
        lo.Statistique(lo)
    elif choix == 0:
        break

