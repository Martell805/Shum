from abc import ABC, abstractmethod


class Generator(ABC):
    def __init__(self, size):
        self.size = size

    def setSize(self, size):
        self.size = size

    def getSize(self):
        return self.size

    @abstractmethod
    def generate_field(self):
        ...
