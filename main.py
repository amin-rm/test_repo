from gpt_ai import *
from text_extractor import *
from text_cleaner import *
from db_management import *
# EMAIL :
messages=messages_recus(2) # extraire une liste de n messages recues avec tous les informations
resultat=generate_chat_response(messages[1]) # AI
etat=mail_data_insertion(resultat) # inserer les données dans un table sql
if etat:
    print("Insersion avec succees")


'''# Extraire et nettoyer les information a partir des images:
images=img_to_text(15651) # une liste des textes extraites a partir d'une liste d'images
for i in images:
    print(clean_text(i))
    print(generate_chat_response(clean_text(i)))
print(type(images))
print(len(images))
'''
# split lel listes wt7othom fi base de donnés