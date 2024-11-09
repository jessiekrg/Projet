from textblob import TextBlob
import json
import re

#PARTIE : CREATION DU TWEET + SOUMISSION DU TWEET DANS LANDING ZONE

#Création d'une Classe Tweet à laquelle seront associées les attributs suivant : auteurs, hashtag, mentions, sentiments, (topics???)
class Tweet: #Plan/Modèle
    def __init__(self, auteur, contenu): #Méthode (assisstant qui aide à donner à chaque tweet ses attributs)
        self.auteur = auteur
        self.contenu = contenu
        self.hashtags = self.Extraction_Hashtags()
        self.mentions = self.Extraction_Mentions()
        self.sentiment = self.Extraction_Sentiments()
    
    def Extraction_Sentiments(): #A Faire (utilisation textblob)
        """"""

        return sentiments
    
    def Extraction_Hashtags():  #A Faire 
        """"""
        hashtags = re.findall(r'#\w+', tweet)
        return hashtags
    
    def Extraction_Mentions():  #A Faire
        """"""
        return Mentions
    

def Nettoyage_Tweet():
    return Tweet_Propre
  
#PARTIE : 