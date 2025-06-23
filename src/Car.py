class Car:
    # Constructor to initialize a Car object with make, model, year, and price
    def __init__(self, make, model, year, price):
        # Normalize make and model to uppercase for consistent comparisons
        self.make = make.upper()
        self.model = model.upper()
        self.year = year
        self.price = price

    # Greater-than comparison operator for sorting or comparing cars
    def __gt__(self, rhs):
        if self.make != rhs.make:
            return self.make > rhs.make
        elif self.model != rhs.model:
            return self.model > rhs.model
        elif self.year != rhs.year:
            return self.year > rhs.year
        else:
            return self.price > rhs.price

    # Less-than comparison operator for sorting or comparing cars
    def __lt__(self, rhs):
        if self.make != rhs.make:
            return self.make < rhs.make
        elif self.model != rhs.model:
            return self.model < rhs.model
        elif self.year != rhs.year:
            return self.year < rhs.year
        else:
            return self.price < rhs.price

    # Equality operator to determine if two cars are the same
    def __eq__(self, rhs):
        if rhs is None:
            return False
        else:
            # Two cars are considered equal if all attributes match
            return (self.make == rhs.make and
                    self.model == rhs.model and
                    self.year == rhs.year and
                    self.price == rhs.price)

    # String representation of the Car object for display
    def __str__(self):
        return "Make: {}, Model: {}, Year: {}, Price: ${}".format(
            self.make, self.model, self.year, self.price
        )
