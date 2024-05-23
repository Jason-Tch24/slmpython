'''fonction detecteNombre(nombre:entier){
    sommeCumuler : entier;
    for(entier i; i<nombre; i++){
        if(n%i == 0){
            sommeCumuler = sommeCumuler + i;
        }
    }
    if(sommeCumuler==1){
        ecrire("Le nombre ", nombre,"est dit premier");
    }else if(sommeCumuler < nombre){
            ecrire("Le nombre ", nombre,"est dit deficient de ", nombre - sommeCumuler);
        }else if(sommeCumuler>nombre){
                ecrire("Le nombre ", nombre,"est dit abondant de ", sommeCumuler - nombre);
            }
}

def detecteNombre(entier) :
    sommeCumuler = 0
    for i in range(1,entier,1) :
        if entier%i == 0:
            sommeCumuler = sommeCumuler+i
    if sommeCumuler == entier :
        print("Le nombre est parfait")
    elif sommeCumuler < entier :
        print("Le nombre est deficient")
    elif sommeCumuler > entier :
        print("Le nombre est abondant")
    if sommeCumuler == 1 :
        print("Le nombre est aussi premier")

nombre = int(input("Entrer un nombre :"))

detecteNombre(nombre)'''
import random
from collections import defaultdict

def lire_fichier(nom_fichier, encodage='utf-8'):
    try:
        with open(nom_fichier, 'r', encoding=encodage) as fichier:
            contenu = fichier.readlines()
        # Enlever les caractères de nouvelle ligne de chaque ligne
        contenu = [ligne.strip() for ligne in contenu]
        return contenu
    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'a pas été trouvé.")
        return None
    except UnicodeDecodeError as e:
        print(f"Erreur de décodage : {e}")
        return None
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
        return None

nom_fichier = 'listemots.txt'
dictmots = lire_fichier(nom_fichier)

if dictmots is not None:
    print("Contenu du fichier stocké dans la liste :")
else:
    print("Impossible de lire le fichier.")

from collections import defaultdict

def construire_dictionnaire_probabilites(liste_mots):
    dico_counts = defaultdict(lambda: defaultdict(int))
    dico_probabilites = defaultdict(dict)

    # Comptage des paires de lettres
    for mot in liste_mots:
        for i in range(len(mot) - 1):
            lettre1 = mot[i]
            lettre2 = mot[i + 1]
            dico_counts[lettre1][lettre2] += 1

    # Calcul des probabilités
    for lettre1, suivies in dico_counts.items():
        total_suivies = sum(suivies.values())
        for lettre2, count in suivies.items():
            dico_probabilites[lettre1][lettre2] = count / total_suivies

    return dico_probabilites


def generer_mot(dico_probabilites, longueur):
    if not dico_probabilites:
        return ""

    # Choisir une lettre de départ au hasard parmi les clés du dictionnaire
    lettre_courante = random.choice(list(dico_probabilites.keys()))
    mot = [lettre_courante]

    while len(mot) < longueur:
        # Récupérer les probabilités des lettres suivantes
        probabilites_suivies = dico_probabilites.get(lettre_courante, {})
        if not probabilites_suivies:
            break

        lettres = list(probabilites_suivies.keys())
        probabilites = list(probabilites_suivies.values())

        # Choisir la prochaine lettre en fonction des probabilités
        lettre_courante = random.choices(lettres, probabilites)[0]
        mot.append(lettre_courante)

    return ''.join(mot)

dictionnaire_probabilites = construire_dictionnaire_probabilites(dictmots)

nouveau_mot = generer_mot(dictionnaire_probabilites, 10)
print(f" {nouveau_mot}")