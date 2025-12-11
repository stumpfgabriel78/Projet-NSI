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
            valeur = input("quel est votre nom")
            self.enfant = Node(valeur)
            return("recommencer pour completer arbre")

        else:
            self.MP = input("voulez vous aller du côté de votre Mere ou Pere ?")
            if self.MP == "Mere":
                mere = input("nom de votre mere")
                self.inserer_recursive(self.enfant,mere)

            elif self.MP == "Pere":
                pere = input("nom de votre pere")
                self.inserer_recursive(self.enfant,pere)

    
    def inserer_recursive(self, noeud, valeur):
        if self.MP == "Pere":
            noeud.pere = node(valeur)

            continuer = input("voulez vous continuer OUI/NON")

            if continuer == "OUI":

                self.MP = input("voulez vous aller du côté de votre Mere ou Pere ?")

                if self.MP == "Mere":
                    mere = input("nom de sa mere")
                    noeud = noeud.mere
                    self.inserer_recursive(noeud.mere,mere)

                elif self.MP == "Pere":
                    pere = input("nom de son pere")
                    noeud = noeud.mere
                    self.inserer_recursive(noeud.pere,pere)
            
            else:
                return("fin arbre genealogique")

        elif self.MP == "Mere":

            noeud.mere = node(valeur)

            continuer = input("voulez vous continuer OUI/NON")

            if continuer == "OUI":

                self.MP = input("voulez vous aller du côté de votre Mere ou Pere ?")

                if self.MP == "Mere":
                    mere = input("nom de sa mere")
                    noeud = noeud.mere
                    self.inserer_recursive(noeud.mere,mere)

                elif self.MP == "Pere":
                    pere = input("nom de son pere")
                    noeud = noeud.mere
                    self.inserer_recursive(noeud.pere,pere)
            
            else:
                return("fin arbre genealogique")


        
         




