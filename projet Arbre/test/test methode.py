import unittest
from classe import Node, ABR, familyMember
class testMethode():
    def __init__(self):
        self.arbre=ABR()

    def addFamilyMember(self):
        AssertIs(self.arbre.addFamilyMemberPartie1("GS"), "GS")

    def search(self):
        self.arbre.addFamilyMemberPartie1("GS")
        AssertIs(self.arbre.addFamilyMemberPartie1("LS", "mere"), "LS")
    
    def print_tree(self):
        AssertIsNotNone(self.arbre.print_tree())


if __name__ == "__main__":
    unittest.main()