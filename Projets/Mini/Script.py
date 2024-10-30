from sentence_transformers import SentenceTransformer 
import numpy as np
import json

modele = SentenceTransformer('paraphrase-MiniLM-L6-v2') #Chargement d'un modèle SBERT

def Charger_Documents(Fichier):
    """Charge les documents/Articles du Fichier et renvoie un dictrionnaire de format {Article (article) : Embeddings (valeur)"""
    Documents_Embeddings = []
    with open(Fichier, 'r') as Fichier:
        indice = 1
        for Document in Fichier:
            embedding = modele.encode(Document)
            embedding = embedding.tolist() # array --> list : json ne peut pas stocker des arrays
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

def Sauvegarde_JSON (Fichier):
    """Sauvegarde les embeddings sous format JSON """
    with open ('data.json','w') as json_file:
        json.dump(Charger_Documents(Fichier),json_file,indent= 4) # stocke les embeddings des documents dans un fichier JSON

def Encoder_Requete(requete):
    """Encode la requête saisie par l'utilisateur"""
    embedding_requete = modele.encode(requete) # convertie la requête en un vecteur 
    return embedding_requete


def cosine_similarity(vector1, vector2):
    """Calcul de la similarité cosinus""" # source : https://medium.com/@santannalouis208/la-similarité-cosinus-en-ia-nlp-d554d3b14efa
    #Produit scalaire des vecteurs
    scalar_product = np.dot(vector1, vector2)
    #Norme euclidienne des vecteurs
    norm_vector1 = np.linalg.norm(vector1)
    norm_vector2 = np.linalg.norm(vector2)
    #Expression analytique du cosinus dans un espace euclidien
    cosine = scalar_product / (norm_vector1 * norm_vector2)
    return cosine

def Similarite_Requete_Document():
    """Calculez la similarité cosinus entre le vecteur de la requête et les vecteurs des documents pour identifier les documents les plus proches"""
    requete_utilisateur = input("Saisir une requête")
    vecteur_requete = Encoder_Requete(requete_utilisateur)
    with open ('data.json',"r") as f:
        loaded_data = json.load(f) # convertion du contenu du fichier JSON en objets python

    for document in loaded_data:
        document["embedding"] = np.array(document["embedding"]) # Reconversion en array 
        if cosine_similarity(document["embedding"] , vecteur_requete) >= 0.8:
            print("Les élements sont similaires")
        elif 0 <= cosine_similarity(document["embedding"] , vecteur_requete) < 0.8:
            print("Les élements ne sont pas similaires")
        elif cosine_similarity(document["embedding"] , vecteur_requete) == -1: # Revoir les intervalles
            print("Les élements ne sont opposés")
    

