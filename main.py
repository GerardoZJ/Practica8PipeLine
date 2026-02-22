class Calculator:
    def sum(self, a: int, b: int) -> int:
        return a + b

    def restar(self, a: int, b: int) -> int:
        return a - b

    # El test espera un método llamado "subtract"
    def subtract(self, a: int, b: int) -> int:
        return self.restar(a, b)

    def multiply(self, a: int, b: int) -> int:
        return a * b

    def divide(self, a: int, b: int) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b