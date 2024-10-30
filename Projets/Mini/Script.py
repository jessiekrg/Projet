from sentence_transformers import SentenceTransformer 
import numpy as np
import json

modele = SentenceTransformer('paraphrase-MiniLM-L6-v2') #Chargement d'un modèle SBERT

def Charger_Documents(Fichier):
    """Charge les documents/Articles du Fichier et renvoie un dictrionnaire de format {Article (article) : Embeddings (valeur)"""
    global Documents_Embeddings
    Documents_Embeddings = []
    with open(Fichier, 'r') as Fichier:
        indice = 1
        for Document in Fichier:
            embedding = modele.encode(Document)
            embedding = embedding.tolist()
            Documents_Embeddings.append({
                "id": indice,
                "texte": Document,
                "embedding" : embedding
            })
            indice+=1
            #print(f'ligne : {Document} , embedding : {embedding}')
            print(Documents_Embeddings)
    return Documents_Embeddings

Charger_Documents('/Users/lnberroug/Documents/LDDBI-L2/Info/IN304/Projet/Projets/Mini/lois.txt')

def Sauvegarde_JSON (data,fichier):
    with open (fichier,'w') as json_file:
        json.dump(data,json_file,indent= 4)

Sauvegarde_JSON(Documents_Embeddings,'data.json')
