class Node:
    def __init__(self, valeur):
        self.valeur = valeur
        self.pere = None
        self.mere = None


class ABR:
    def __init__(self):
        self.enfant = None

    def inserer(self):
        if self.enfant is None:
            valeur = input("Quel est votre nom ? ")
            self.enfant = Node(valeur)
            print("Recommencer pour compléter l'arbre")
        else:
            cote = input("Voulez-vous aller du côté de votre Mere ou Pere ? ").lower()
            if cote == "mere":
                mere = input("Nom de votre mère : ")
                self.enfant.mere = Node(mere)
                self.inserer_recursive(self.enfant.mere)
            elif cote == "pere":
                pere = input("Nom de votre père : ")
                self.enfant.pere = Node(pere)
                self.inserer_recursive(self.enfant.pere)

    def inserer_recursive(self, noeud):
        continuer = input("Voulez-vous continuer OUI/NON ? ").lower()
        if continuer != "oui":
            print("Fin de l'arbre généalogique")
            return

        cote = input("Voulez-vous aller du côté de sa Mere ou de son Pere ? ").lower()

        if cote == "mere":
            mere = input("Nom de sa mère : ")
            noeud.mere = Node(mere)
            self.inserer_recursive(noeud.mere)

        elif cote == "pere":
            pere = input("Nom de son père : ")
            noeud.pere = Node(pere)
            self.inserer_recursive(noeud.pere)




