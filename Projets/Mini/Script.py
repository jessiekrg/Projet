from sentence_transformers import SentenceTransformer 
import numpy as np

modele = SentenceTransformer('paraphrase-MiniLM-L6-v2') #Chargement d'un modèle SBERT

def Charger_Documents(Fichier):
    """Charge les documents/Articles du Fichier et renvoie une liste ou tableau des embeddings respectif"""
    with open(Fichier, 'r') as Fichier:
        for Document in Fichier:
            embedding = modele.encode(Document)
            print(f'ligne : {Document} , embedding : {embedding}')
            
    return embedding

Charger_Documents('Projets/Mini/lois.txt')