# Car Inventory Project

## Overview

This project implements a **Car Inventory Management System** using a **Binary Search Tree (BST)** data structure. It allows you to efficiently add, remove, and search cars in an inventory, where cars are organized by make and model.

Each node in the tree can hold multiple cars of the **same make and model** but different years and prices.

---

## Why?

Managing a car inventory efficiently is essential for:

- **Dealerships and sellers**: Quickly searching and organizing cars by make and model helps manage stock and pricing strategies.
- **Buyers**: Enables fast lookup of available cars matching specific criteria (make, model, year, price).
- **Developers and learners**: Demonstrates practical use of binary search trees in real-world data management.
- **Scalability**: The BST structure supports efficient insertions, deletions, and searches even as the inventory grows.

This project helps explore data structures and algorithms through a practical and relatable example.

---

## Features

- Add new cars to the inventory
- Search if a specific car exists
- Retrieve the best or worst car of a given make and model (based on year and price)
- Remove cars from the inventory
- List inventory in different traversal orders (in-order, pre-order, post-order)
- Calculate the total price value of all cars in inventory

---

## Code Structure

- **Car.py**: Defines the `Car` class with attributes like make, model, year, and price. Includes comparison methods to enable sorting.
- **CarInventoryNode.py**: Defines the `CarInventoryNode` class that extends `Car` and serves as a node in the BST, holding a list of cars with the same make and model.
- **CarInventory.py**: Implements the binary search tree managing the car inventory, with methods to insert, search, remove, and traverse nodes.

---

## Usage

1. **Create a Car object:**

```python
from Car import Car
car = Car("Tesla", "Model 3", 2020, 45000)
