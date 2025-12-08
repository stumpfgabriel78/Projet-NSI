class Node:
    def __init__(self, valeur):
        self.valeur = valeur
        self.pere = None
        self.mere = None

class ABR:
    def __init__(self):
        self.enfant = None


arbre = ABR()
arbre.enfant = Node("Nathan")
arbre.enfant.pere = Node("JJ")
arbre.enfant.mere = Node("Helene")
print (value(arbre.enfant.mere))