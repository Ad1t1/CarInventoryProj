from CarInventory import CarInventory
from Car import Car

def main():
    inventory = CarInventory()
    car1 = Car("Mazda", "CX-5", 2022, 25000)
    inventory.addCar(car1)
    print(inventory.inOrder())

if __name__ == "__main__":
    main()
