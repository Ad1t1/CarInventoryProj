from Car import *


class CarInventoryNode(Car):
    """
    Represents a node in the car inventory binary search tree.
    Inherits from the Car class to store make and model as sorting keys.
    """

    def __init__(self, car):
        # Initialize using Car's constructor to inherit make, model, etc.
        super().__init__(car.make, car.model, car.year, car.price)
        
        # List of car objects with same make and model (can differ by year/price)
        self.cars = [car]

        # Pointers for tree structure
        self.parent = None
        self.left = None
        self.right = None

    # Getter for car make
    def getMake(self):
        return self.make

    # Getter for car model
    def getModel(self):
        return self.model

    # Getter for parent node
    def getParent(self):
        return self.parent

    # Setter for parent node
    def setParent(self, parent):
        self.parent = parent

    # Getter for left child
    def getLeft(self):
        return self.left

    # Setter for left child
    def setLeft(self, left):
        self.left = left

    # Getter for right child
    def getRight(self):
        return self.right

    # Setter for right child
    def setRight(self, right):
        self.right = right

    # String representation of the node showing all cars at this node
    def __str__(self):
        s = ""
        if not self.cars:
            return s
        
        for c in self.cars:
            s += str(c) + "\n"
        return s
