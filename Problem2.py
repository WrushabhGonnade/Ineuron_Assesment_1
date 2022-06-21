# 2 Demonstrate use of abstract class, multiple inheritance and decorator in python using examples.
from abc import ABC, abstractmethod


class Bank(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @abstractmethod
    def get_amount(self):
        pass


class Amount_without_Interest(Bank):
    def __init__(self, first_name, last_name, rupee):
        super().__init__(first_name, last_name)
        self.rupee = rupee

    def get_amount(self):
        return self.rupee


class Amount_with_Interest(Bank):
    def __init__(self, first_name, last_name, rupee, interest):
        super().__init__(first_name, last_name)
        self.rupee = rupee
        self.interest = interest

    def get_amount(self):
        return self.rupee + (self.rupee / 100) * self.interest


SBI = Amount_with_Interest('Wrushabh', 'Gonnade', 500, 10)
print("Name: ", SBI.full_name())
print("Amount with {} % Interest is Rs: {}".format(SBI.interest, SBI.get_amount()))

BOB = Amount_without_Interest('Wrushabh', 'Gonnade', 500)
print("Name: ", BOB.full_name())
print("Amount without Interest is Rs: ", BOB.get_amount())