from classe import  Node, ABR, familyMember
continu = True
arbre = ABR()
print("____________________________\nbienvenue commencons votre arbre genalogique ! \n____________________________\n")
print("____________________________\ncommencons par vous!")
actual_name = input("votre nom prenom ")
actual_date = str(input("votre date de naissance"))
print("____________________________")
arbre.addFamilyMember(familyMember(actual_name,actual_date))
while continu == True:
    entry = input("____________________________\nvoulez vous continuez d'ajouter des membres? o = oui n=non")
    if entry != "o" and entry !="n":
         entry = input("voulez vous continuez d'ajouter des memebres? o = oui n=non")
    elif entry == "n":
         break
    else:
         actual_name = input("__________________________\n le nom prenom ")
         actual_date = str(input("la date de naissance "))
         actual_refer = input("membre au quel il se ratache ")
         actual_fonction = input("pere ou mere")
         print("________________________")
         arbre.addFamilyMember(familyMember(actual_name,actual_date),actual_refer,actual_fonction)
arbre.print_tree()

