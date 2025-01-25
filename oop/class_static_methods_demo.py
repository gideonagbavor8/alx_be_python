class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Returns the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Prints the calculation type and returns the product of two numbers."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
