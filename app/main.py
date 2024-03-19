from typing import Union
import math
from app.error import InvalidInputException

numeric = Union[int, float]


class Calculator:

    @staticmethod
    def sum(*args):
        for arg in args:
            if not isinstance(arg, numeric):
                raise TypeError
        return sum(args)

    @staticmethod
    def subtract(a: numeric, b: numeric) -> numeric:
        return a - b

    @staticmethod
    def multiply(a: numeric, b: numeric) -> numeric:
        return a * b

    @staticmethod
    def divide(a: numeric, b: numeric) -> numeric:
        return a / b

    def log(self, a: numeric, base: numeric) -> numeric:
        if not (isinstance(a, numeric) and isinstance(base, numeric)):
            raise InvalidInputException('The inputs must be numeric')

        if a > 0 and a != 1 and base > 0:
            return math.log(a, base)
        else:
            raise InvalidInputException('Invalid input for log function')

