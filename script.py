import datetime
import os


# repurere les fichieers d'extension proposer

def filtre_extension(fichiers , extensions):
    fichier_filter = []
    if extensions:
        for fichier in fichiers : 
            if fichier.split(".")[-1] in extensions : 
                fichier_filter.append(fichier)
        return fichier_filter
    
    return fichiers  


# Fonction pour vérifier si un fichier appartient à une année donnée

# creetion d"un fonction pour recuperer le chemin d'acces des fichiers a trier

def est_fichier(dateFichier, annee)->bool:
    annee_fichier = int(datetime.datetime.strftime(dateFichier,"%Y"))
    
    if annee[0]<=annee_fichier<=annee[1] or annee[0]>=annee_fichier>=annee[1] or annee[0]==annee_fichier==annee[1]:
        print("ok",annee)
        return True
    
    return False

# Fonction pour archiver les fichiers appartenant à une année donnée
def archiver_fichiers(directory, archive, annee , extension = None):
    # Vérifier si le répertoire d'archivage existe, sinon le créer
    if not os.path.exists(archive):
        os.mkdir(archive)

    element = [] 
    for elem in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, elem)):
            continue
        element.append(elem)

    liste_fichiers_annee = []
    # Parcourir les fichiers dans le répertoire donné
    for fichier in element:
        date_fichier_float = os.path.getmtime(os.path.join(directory, fichier))
        date_fichier = datetime.datetime.utcfromtimestamp(date_fichier_float).date()
        # Vérifier si le fichier appartient à l'année spécifiée
        if est_fichier(date_fichier, annee):
            liste_fichiers_annee.append(fichier)


    # #debug
    # print("debug 1",liste_fichiers_annee)
    
    #selectionner les extentions 
    liste_fichiers_annee = filtre_extension(liste_fichiers_annee , extension)

    #debug
    print("debug 2",liste_fichiers_annee)
    
    # Pour archiver les fichiers dans le répertoire d'archivage
    for fichier in liste_fichiers_annee:
        os.rename(os.path.join(directory, fichier), os.path.join(archive, fichier))
        print(f"Fichier {fichier} archivé dans {archive}")


