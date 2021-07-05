from pprint import pprint
from time import sleep
from sys import argv

def octets_total():
    fichier = open("/proc/net/dev")
    donnees = fichier.read()

    lignes = donnees.splitlines()

    for ligne in lignes:
        if ligne.startswith("wlp8s0:"):
            mots = ligne.split()
            octets_recus = int(mots[1])
            octets_envoyes = int(mots[9])
            return octets_recus + octets_envoyes


def debit():
    duree_delai = float(argv[1])
    total_avant = octets_total()

    sleep(duree_delai)
    total_apres = octets_total()
    difference = total_apres - total_avant

    return difference / duree_delai


fichier = open("resultats.csv", "w")

for i in range(20):
    fichier.write(str(round(debit())))
    fichier.write("\n")


"""
while True:
    largeur = 80
    debit_actuel = debit()
    debit_max = 6_000_000
    nombre_caracteres = round(largeur * debit_actuel / debit_max)
    print("\033c")
    print(
        "[",
        nombre_caracteres * "#",
        (largeur - nombre_caracteres) * " ",
       "] ",
       debit_actuel,
       sep=""
    )
"""
