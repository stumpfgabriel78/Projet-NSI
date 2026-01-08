import unittest
from classe import Node, ABR, familyMember
class testMethode():
    def __init__(self):
        self.arbre=ABR()

    def addFamilyMember(self):
        self.arbre.addFamilyMember("GS")

    def search(self):
        self.arbre.search("GS")
    
    def print_tree(self):
        self.arbre.print_tree()


if __name__ == "__main__":
    unittest.main()