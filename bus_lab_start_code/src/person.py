class Person:
    def __init__(self, name, age, cash):
        self.name = name
        self.age = age
        self.cash = cash


    def reduce_cash(self, amount):
        self.cash -= amount
