from classe import  Node, ABR, familyMember
import pickle
import os 

#definie la valeur de continue
continu = True

print("____________________________\nbienvenue commencons votre arbre genalogique ! \n____________________________\n")
print ("____________________________\n")
entry = "b"
#verifie les entrees
while entry != "n" and entry != "o":
     entry = input("avez vous deja un arbre en cours o = oui n =non")

#si il veut recomencer 

if entry == "n": 
     #on supprime au cas ou pour pas creer de conflit ou de problemes entre plusieurs fichiers data
     try:
          os.remove("data/arbre.pkl")
     except:
          None
     arbre = ABR()
     print("____________________________\ncommencons par vous!")
     actual_name = input("votre nom prenom ")
     actual_date = str(input("votre date de naissance"))
     print("____________________________")
     arbre.addFamilyMember(familyMember(actual_name,actual_date))
#sinonil y a un fichier


else:
     try:
          #ouvrir le fichier pour le modifier
          with open("data/arbre.pkl", "rb") as f:
               arbre = pickle.load(f)
          arbre.print_tree()
     #au cas ou il n'y a pas de fichier
     except:
          print("Oops vous n'avez pas d'arbre en cours")


while continu == True:

     entry = "b"

     while entry != "n" and entry != "o":
          entry = input("____________________________\nvoulez vous continuez d'ajouter des membres? o = oui n=non")

     #si il veut pas continuer
     if entry == "n":  
          break 


     else:
         actual_fonction = None 
         actual_name = input("__________________________\n le nom prenom ")
         actual_date = str(input("la date de naissance "))
         actual_refer = input("memebre au quel il se ratache ")
         while actual_fonction != "pere" and actual_fonction != "mere":
               actual_fonction = input("pere ou mere")
         print("________________________")
         arbre.addFamilyMember(familyMember(actual_name,actual_date),actual_refer,actual_fonction)
arbre.print_tree()
#supprime le ficier avant de sauver
try:
     os.remove("data/arbre.pkl")
     print("__________________________\nSAUVEGARDER\n__________________________")
except:
     print("__________________________\nSAUVEGARDER\n__________________________")
#sauvegarde
with open("data/arbre.pkl", "wb") as f:
    pickle.dump(arbre, f)

