#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price
        self.status = "hot"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def sip(self):
        print(f"You take a sip of the {self.size} coffee.")

    def finish(self):
        self.status = "finished"
        print(f"You finished your {self.size} coffee.")

    def tip(self):
        self.price += 1
        print("This coffee is great, here’s a tip!")
