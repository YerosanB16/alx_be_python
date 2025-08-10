class Calculator:
    calculation_type = "Arithmetic Operations"  # Class attribute

    @staticmethod
    def add(a, b):
        """Static method to add two numbers."""
        return a + b

    @classmethod
    def calc_type(cls):
        """Class method to return calculation type."""
        return cls.calculation_type

    @staticmethod
    def multiply(a, b):
        """Static method to multiply two numbers."""
        return a * b
