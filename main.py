class Calculator:
    def sum(self, a: int, b: int) -> int:
        return a - b  # ERROR intencional

    def restar(self, a: int, b: int) -> int:
        return a + b  # ERROR intencional

    def multiply(self, a: int, b: int) -> int:
        return a + b  # ERROR intencional

    def divide(self, a: int, b: int) -> float:
        return a / b  # ERROR: no maneja división entre 0