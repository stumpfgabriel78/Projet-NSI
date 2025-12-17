class Node:
    def __init__(self, valeur):
        self.valeur = valeur
        self.pere = None
        self.mere = None
        self.MP = None


class ABR:
    def __init__(self):
        self.enfant = None
   
    def inserer(self):
        if self.enfant == None:
            valeur = input("quel est votre nom \n")
            self.enfant = Node(valeur)
            return print("recommencer pour completer arbre\n")


        else:
            self.MP = input("voulez vous aller du côté de votre Mere ou Pere ?\n")
            while self.MP != "Pere" and self.MP != "Mere":
                    print("verifier la valeur")
                    self.MP = input("voulez vous aller du côté de votre Mere ou Pere ?\n")
            if self.MP == "Mere":
                mere = input("nom de votre mere\n")
                self.inserer_recursive(self.enfant,mere)


            elif self.MP == "Pere":
                pere = input("nom de votre pere")
                self.inserer_recursive(self.enfant,pere)


   
    def inserer_recursive(self, noeud, valeur):
       
        if self.MP == "Pere":
            if noeud.mere is None:
                noeud.mere = Node(pere)
            else:
                self.inserer_recursive(noeud.pere, valeur)



            """continuer = input("voulez vous continuer OUI/NON")
            while continuer != "OUI" and continuer != "NON":
                    print("verifier la valeur")
                    continuer = input("voulez vous continuer OUI NON ?")
            if continuer == "OUI":


                self.MP = input("voulez vous aller du côté de votre Mere ou Pere ?")


                if self.MP == "Mere":
                    mere = input("nom de sa mere")
                    noeud = Node.mere
                    self.inserer_recursive(noeud.mere,mere)


                elif self.MP == "Pere":
                    pere = input("nom de son pere")
                    noeud = Node.pere
                    self.inserer_recursive(noeud.pere,pere)
           
            else:
                return("fin arbre genealogique")"""


        elif self.MP == "Mere":
            if noeud.mere is None:
                noeud.mere = Node(mere)
            else:
                self.inserer_recursive(noeud.pere, valeur)



            


            """continuer = input("voulez vous continuer OUI/NON")
            while continuer != "OUI" and continuer != "NON":
                    print("verifier la valeur")
                    continuer = input("voulez vous continuer OUI NON ?")
            if continuer == "OUI":


                self.MP = input("voulez vous aller du côté de votre Mere ou Pere ?")


                if self.MP == "Mere":
                    mere = input("nom de sa mere")
                    noeud = Node.mere
                    self.inserer_recursive(noeud.mere,mere)


                elif self.MP == "Pere":
                    pere = input("nom de son pere")
                    noeud = Node.pere
                    self.inserer_recursive(noeud.pere,pere)
           
            else:
                return("fin arbre genealogique")"""

arbre=ABR()
arbre.inserer()
arbre.inserer()
arbre.inserer()




