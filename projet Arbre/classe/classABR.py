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
    def print_tree(self, node=None, prefix=""):
        if node is None:
            node = self.root
        if node is None:
            print("L'arbre est vide")
            return

        # imprimer le nom du noeud courant (racine ou sous-noeud si appelé directement)
        print(prefix + node.valeur.Name)

        # construire la liste d'enfants (Père, Mère)
        children = []
        if node.pere:
            children.append(("Père", node.pere))
        if node.mere:
            children.append(("Mère", node.mere))

        # pour chaque enfant, on imprime la ligne relation (connecteur + rôle + nom)
        # puis on descend récursivement pour afficher ses descendants
        for i, (role, child) in enumerate(children):
            is_last = (i == len(children) - 1)
            connector = "└─ " if is_last else "├─ "
            # affiche la ligne qui relie le parent à cet enfant, avec le rôle
            print(prefix + connector + role + " : " + child.valeur.Name)
            # extension d'indentation pour les descendants
            extension = "    " if is_last else "│   "
            # descend pour afficher les enfants du child (sans ré-imprimer child.valeur.Name ici)
            self._print_subtree(child, prefix + extension)

    # helper qui imprime uniquement les descendants (les lignes relation) d'un noeud dont
    # la ligne principale (nom) a déjà été affichée
    def _print_subtree(self, node, prefix):
        children = []
        if node.pere:
            children.append(("Père", node.pere))
        if node.mere:
            children.append(("Mère", node.mere))

        for i, (role, child) in enumerate(children):
            is_last = (i == len(children) - 1)
            connector = "└─ " if is_last else "├─ "
            print(prefix + connector + role + " : " + child.valeur.Name)
            extension = "    " if is_last else "│   "
            self._print_subtree(child, prefix + extension)