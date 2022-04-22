from .Generator import Generator
import numpy


class SinGenerator(Generator):
    def __generate_cell(self, q, w):
        cell = abs(self.getSize() / 2 - w) + abs(self.getSize() / 2 - q)
        cell = numpy.sin(cell / 10) * 100 + numpy.random.randint(-50, 50, (self.getSize(), self.getSize()))
        return numpy.clip(cell, -255, 255)

    def generate_field(self):
        new_field = numpy.fromfunction(self.__generate_cell, (self.getSize(), self.getSize()))

        return new_field
