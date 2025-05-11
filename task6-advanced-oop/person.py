from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name: str, age: int, **kwargs):
        self.name = name
        self.age = age

    @abstractmethod
    def get_role(self) -> str:
        pass