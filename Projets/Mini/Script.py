from sentence_transformers import SentenceTransformer 
import numpy as np

modele = SentenceTransformer('paraphrase-MiniLM-L6-v2') #Chargement d'un modèle SBERT

def Charger_Documents(Fichier):
    """Charge les documents/Articles du Fichier et renvoie un dictrionnaire de format {Article (article) : Embeddings (valeur)"""
    Documents_Embeddings = {}
    with open(Fichier, 'r') as Fichier:
        for Document in Fichier:
            embedding = modele.encode(Document)
            Documents_Embeddings[Document] = embedding
            #print(f'ligne : {Document} , embedding : {embedding}')
            print(Documents_Embeddings)
    return Documents_Embeddings

Charger_Documents('Projets/Mini/lois.txt')