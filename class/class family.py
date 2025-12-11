#1 creer une class membre de la famille
class familyMember ():
    def __init__(self,name,firstName,bornDate):
        self.name = name
        self.firstName = firstName
        self.bornDate = bornDate


#2 organisation en arbre
class Node:
    def __init__(self, valeur):
        self.valeur = valeur
        self.pere = None
        self.mere = None


class ABR:
    def __init__(self):
        self.enfant = None
#test
myTree = ABR()
myTree.enfant = familyMember("Ethan","Durvin","13/09/2008")
myTree.enfant.pere = familyMember("jean","Durvin","06/07/1985")
myTree.enfant.pere.pere = familyMember("David","Durvin","03/08/1930")
