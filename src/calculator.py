# A simple calculator.


class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a: float, b: float) -> float:
        result = float(a) + float(b)
        self.history.append(f"{a} + {b} = {result}")

        return result

    def subtract(self, a: float, b: float) -> float:
        result = float(a) - float(b)
        self.history.append(f"{a} - {b} = {result}")

        return result

    def multiply(self, a: float, b: float) -> float:
        result = float(a) * float(b)
        self.history.append(f"{a} * {b} = {result}")

        return result

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")

        result = float(a) / float(b)
        self.history.append(f"{a} / {b} = {result}")

        return result

    def power(self, base: float, exponent: float) -> float:
        result = float(float(base) ** float(exponent))
        self.history.append(f"{base} ^ {exponent} = {result}")

        return result

    def get_history(self) -> list:
        return self.history.copy()

    def clear_history(self) -> None:
        self.history.clear()


def main():
    calc = Calculator()

    print("Calculator Demo")
    print("=" * 50)

    # Perform calculations
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 5 = {calc.subtract(10, 5)}")
    print(f"10 * 5 = {calc.multiply(10, 5)}")
    print(f"10 / 5 = {calc.divide(10, 5)}")
    print(f"2 ^ 8 = {calc.power(2, 8)}")

    print("\nHistory:")
    for operation in calc.get_history():
        print(f"  {operation}")


if __name__ == "__main__":
    main()
