import pytest
from app.Calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 3, 3) ==9

    def test_division_calculate_correctly(self):
        assert  self.calc.division(self, 10, 2) ==5

    def test_subtraction_calculate_correctly(self):
        assert  self.calc.subtraction(self, 8, 3) ==5

    def test_adding_calculate_correctly(self):
        assert  self.calc.adding(self, 6, 1) ==7

