from .classFamilyMember import familyMember
#classe node avec donc un pere est une mere
class Node:
    def __init__(self, family_member):
        self.valeur = family_member
        self.pere = None
        self.mere = None
#class arbre qui gere l'arbre familiale
class ABR:
    def __init__(self):
        self.root = None
    #methode search utile pour l'utilisateur mais aussi pour trouver le noueud dans lequel ajouter la valeur
    def search(self, node, name):
        #si le noueud est vide
        if node is None:
            return None
        #si ca correspond
        if node.valeur.Name == name:
            return node
        #sinon on voit du cote du pere
        found = self.search(node.pere, name)
        if found is not None:
            return found
        #puit celui de la mere
        else:
            return self.search(node.mere, name)
    #ajouter un individu a l'arbre
    def addFamilyMember(self, family_member, place=None, function=None):
        #soit la racine est vide donc racine = valeur
        if self.root is None:
            self.root = Node(family_member)
            return
        #sinon on cherche le noueud auqul il se ratache via place
        parent_node = self.search(self.root, place)
        #si il ne touve pas
        if parent_node is None:
            print("Personne non trouvée")
            return
        #si la fonction est pere,
        if function == "pere":
            parent_node.pere = Node(family_member)
        #si c'est mere
        elif function == "mere":
            parent_node.mere = Node(family_member)
     #imprimer l'arbre en console moi + CHAT GPT   
    def print_tree(self, node=None, indent=""):
        if node is None:
            node = self.root
        if node is None:
            print("L'arbre est vide")
            return

        print(indent + node.valeur.Name)

        children = []
        if node.pere:
            children.append(("Père", node.pere))
        if node.mere:
            children.append(("Mère", node.mere))

        for i, (role, child) in enumerate(children):
            if i == len(children) - 1:
                branch = "└─" + role + "─ "
                new_indent = indent + "    "
            else:
                branch = "├─" + role + "─ "
                new_indent = indent + "│   "
            self.print_tree(child, new_indent + branch)