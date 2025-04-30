import pyshark
import csv

def convertir_pcap_en_csv(fichier_pcap, fichier_csv, champs_selectionnes=None, max_paquets=10000):
    """
    Convertit un fichier .pcap en .csv en extrayant les champs réseau principaux.
    
    :param fichier_pcap: Chemin vers le fichier .pcap
    :param fichier_csv: Chemin de sortie pour le fichier .csv
    :param champs_selectionnes: Liste des champs à extraire
    :param max_paquets: Limite du nombre de paquets à traiter
    """
    print(f"Ouverture du fichier : {fichier_pcap}")
    capture = pyshark.FileCapture(fichier_pcap, only_summaries=False)

    champs_defaut = ['frame.number', 'frame.time', 'ip.src', 'ip.dst', 'frame.len', 'frame.protocols']
    champs = champs_selectionnes if champs_selectionnes else champs_defaut

    with open(fichier_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(champs)

        for i, paquet in enumerate(capture):
            if i >= max_paquets:
                break
            ligne = []
            for champ in champs:
                try:
                    valeur = paquet.get_multiple_layers_field(champ)[0]
                except:
                    valeur = ''
                ligne.append(valeur)
            writer.writerow(ligne)

    print(f"✅ Fichier converti avec succès : {fichier_csv}")

# Exemple d'utilisation
convertir_pcap_en_csv("exemple.pcap", "sortie.csv")
