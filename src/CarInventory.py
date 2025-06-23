from Car import *
from CarInventoryNode import *


class CarInventory(CarInventoryNode):
    def __init__(self):
        # Initialize the root of the inventory (BST)
        self.root = None

    def addCar(self, car):
        # Add a new car to the inventory tree
        if self.root is None:
            self.root = CarInventoryNode(car)
        else:
            self.insertCar(car, self.root)

    def insertCar(self, car, currentNode):
        # Recursive insertion of a car into the correct node in BST
        if car.make == currentNode.make and car.model == currentNode.model:
            # Same make and model, add to this node's car list
            currentNode.cars.append(car)
        elif (car.make == currentNode.make and car.model < currentNode.model) or car.make < currentNode.make:
            # Go left
            if currentNode.getLeft() is None:
                nextNode = CarInventoryNode(car)
                currentNode.setLeft(nextNode)
                nextNode.setParent(currentNode)
            else:
                self.insertCar(car, currentNode.getLeft())
        else:
            # Go right
            if currentNode.getRight() is None:
                nextNode = CarInventoryNode(car)
                currentNode.setRight(nextNode)
                nextNode.setParent(currentNode)
            else:
                self.insertCar(car, currentNode.getRight())

    def doesCarExist(self, car):
        # Public method to check car existence
        return self.carExists(car, self.root)

    def carExists(self, car, currentNode):
        # Recursively check if car exists in inventory
        if currentNode is None:
            return False

        for c in currentNode.cars:
            if c == car:
                return True

        # Traverse BST depending on comparison
        if car < currentNode.cars[0]:
            return self.carExists(car, currentNode.getLeft())
        else:
            return self.carExists(car, currentNode.getRight())

    def inOrder(self):
        # In-order traversal of BST
        return self.orderCheck(self.root)

    def orderCheck(self, currentNode):
        # Helper: in-order (Left, Node, Right)
        s = ""
        if currentNode is None:
            return s
        s += self.orderCheck(currentNode.getLeft())
        for c in currentNode.cars:
            s += str(c) + "\n"
        s += self.orderCheck(currentNode.getRight())
        return s

    def preOrder(self):
        # Pre-order traversal
        return self.preOrderHelper(self.root)

    def preOrderHelper(self, currentNode):
        s = ""
        if currentNode is None:
            return s
        for c in currentNode.cars:
            s += str(c) + "\n"
        s += self.preOrderHelper(currentNode.getLeft())
        s += self.preOrderHelper(currentNode.getRight())
        return s

    def postOrder(self):
        # Post-order traversal
        return self.postOrderHelper(self.root)

    def postOrderHelper(self, currentNode):
        s = ""
        if currentNode is None:
            return s
        s += self.postOrderHelper(currentNode.getLeft())
        s += self.postOrderHelper(currentNode.getRight())
        for c in currentNode.cars:
            s += str(c) + "\n"
        return s

    def getBestCar(self, make, model):
        # Get the best car of a given make/model (latest year, highest price)
        return self.bestCar(make, model, self.root)

    def bestCar(self, make, model, currentNode):
        if currentNode is None:
            return None
        elif currentNode.make.upper() == make.upper() and currentNode.model.upper() == model.upper():
            best = currentNode.cars[0]
            for c in currentNode.cars:
                if best is None or c.year > best.year or (c.year == best.year and c.price > best.price):
                    best = c
            return best
        elif (make.upper() == currentNode.make.upper() and model.upper() > currentNode.model.upper()) or make.upper() > currentNode.make.upper():
            return self.bestCar(make, model, currentNode.getRight())
        else:
            return self.bestCar(make, model, currentNode.getLeft())

    def getWorstCar(self, make, model):
        # Get the worst car of a given make/model (oldest year, lowest price)
        return self.worstCar(self.root, make, model)

    def worstCar(self, currentNode, make, model):
        if currentNode is None:
            return None
        elif currentNode.make.upper() == make.upper() and currentNode.model.upper() == model.upper():
            worst = None
            for c in currentNode.cars:
                if worst is None or c.year < worst.year or (c.year == worst.year and c.price < worst.price):
                    worst = c
            return worst
        elif (make.upper() == currentNode.make.upper() and model.upper() < currentNode.model.upper()) or make.upper() < currentNode.make.upper():
            return self.worstCar(currentNode.getLeft(), make, model)
        else:
            return self.worstCar(currentNode.getRight(), make, model)

    def getTotalInventoryPrice(self):
        # Get total value of all cars in the inventory
        return self.priceCalculation(self.root)

    def priceCalculation(self, currentNode):
        priceTotal = 0
        if currentNode is None:
            return priceTotal
        for c in currentNode.cars:
            priceTotal += c.price
        priceTotal += self.priceCalculation(currentNode.getLeft())
        priceTotal += self.priceCalculation(currentNode.getRight())
        return priceTotal

    def getSuccessor(self, make, model):
        # Find the in-order successor of a given car make/model
        currentNode = self.getNode(self.root, make, model)
        if currentNode is None:
            return None
        if currentNode.getRight():
            return self.getMinimum(currentNode.getRight())
        return self.findSuccessor(make, model)

    def getNode(self, currentNode, make, model):
        # Find the node matching make and model
        if currentNode is None:
            return None
        if currentNode.make.upper() == make.upper() and currentNode.model.upper() == model.upper():
            return currentNode
        if make.upper() < currentNode.make.upper() or (make.upper() == currentNode.make.upper() and model.upper() < currentNode.model.upper()):
            return self.getNode(currentNode.getLeft(), make, model)
        return self.getNode(currentNode.getRight(), make, model)

    def getMinimum(self, currentNode):
        # Get node with minimum (leftmost) value in a subtree
        current = currentNode
        while current.getLeft():
            current = current.getLeft()
        return current

    def findSuccessor(self, make, model):
        # Find successor without using right child
        s = None
        currentNode = self.root
        while currentNode is not None:
            if make.upper() < currentNode.make.upper() or (make.upper() == currentNode.make.upper() and model.upper() < currentNode.model.upper()):
                s = currentNode
                currentNode = currentNode.getLeft()
            else:
                currentNode = currentNode.getRight()
        return s

    def removeCar(self, make, model, year, price):
        # Public method to remove a car
        carRemoval = Car(make, model, year, price)
        return self.removeCarNode(self.root, carRemoval)

    def removeCarNode(self, currentNode, carRemoval):
        # Remove a specific car from a node; delete node if empty
        if currentNode is None:
            return False

        if carRemoval in currentNode.cars:
            currentNode.cars.remove(carRemoval)
            if not currentNode.cars:
                self.root = self.removeNode(self.root, currentNode)
            return True
        elif carRemoval < currentNode:
            return self.removeCarNode(currentNode.getLeft(), carRemoval)
        else:
            return self.removeCarNode(currentNode.getRight(), carRemoval)

    def removeNode(self, currentNode, removalNode):
        # Remove a node from the tree (handles 0, 1, 2 children cases)
        if currentNode is None:
            return None
        if removalNode < currentNode:
            currentNode.left = self.removeNode(currentNode.getLeft(), removalNode)
        elif removalNode > currentNode:
            currentNode.right = self.removeNode(currentNode.getRight(), removalNode)
        else:
            # Node with 0 or 1 child
            if currentNode.getLeft() is None:
                return currentNode.getRight()
            elif currentNode.getRight() is None:
                return currentNode.getLeft()
            # Node with 2 children
            else:
                minim = self.findMinimum(currentNode.getRight())
                currentNode.make = minim.make
                currentNode.model = minim.model
                currentNode.cars = minim.cars
                currentNode.right = self.removeNode(currentNode.getRight(), minim)
        return currentNode

    def findMinimum(self, currentNode):
        # Helper to find minimum node (leftmost)
        current = currentNode
        while current.left is not None:
            current = current.left
        return current
