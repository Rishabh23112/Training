"""Oops Fundamentals"""

from typing import Any


class Person:
    """Person class for learning encapsulation , dunder methods"""

    species: str = "Homo Sapiens"  # class attribute

    def __init__(self) -> None:
        """constructor"""
        self.name = "Abc"  # instance attribute
        self.age = 21
        self.name1 = "Abc"
        self.__aadhar = 1234567890  # Private
        self.__phone = 111111

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        """Bypasses __str__ and __repr__"""
        return f"My name is {self.name} and I am {self.age}."

    def __str__(self) -> Any:
        """Shows the human readable string."""
        return f"hello using __str__ to print :{self.name}"

    def __repr__(self) -> Any:
        """Show the data (mainly used for logs)"""
        return f"using __repr__ to print : {self.age}"

    def __eq__(self, value: object) -> bool:
        """For comparision, == implements the same."""
        if isinstance(value, Person):
            return value.name1 == self.name
        return False

    # Encapsulation

    def get_aadhar(self) -> int:
        """To access the private attribute. getter"""
        return self.__aadhar

    def set_aadhar(self) -> None:
        """To change the private attribute. setter"""
        self.__aadhar = 12345

    @property
    def phone(self) -> int:
        """same work using property decorator . getter"""
        return self.__phone

    @phone.setter
    def phone(self, new_number: int) -> None:
        """same work using property decorator . setter"""
        self.__phone = new_number


p = Person()
p1 = Person()
print(p)
print([p])
print(p())
print(p == p1)
print(p.set_aadhar())
print(p.get_aadhar())
print(p.phone)
NEW = 22222
p.phone = NEW
print(p.phone)
