class simpleCalculator:
    num1 = 0
    num2 = 0

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def multiply(self):
        return self.num1 * self.num2

    def sum(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def divide(self):
        return self.num1 / self.num2


try:
    numberInput = input("Enter process Format: (%x %symbol %y): ")
    number = numberInput.split()
    symbol = number[1]

    if symbol == "+":
        result = simpleCalculator(int(number[0]), int(number[2])).sum()
        print(f"Result {result}")
    if symbol == "-":
        result = simpleCalculator(int(number[0]), int(number[2])).subtraction()
        print(f"Result {result}")
    if symbol == "/":
        result = simpleCalculator(int(number[0]), int(number[2])).divide()
        print(f"Result {result}")
    if symbol == "x":
        result = simpleCalculator(int(number[0]), int(number[2])).multiply()
        print(f"Result {result}")
    if symbol == "*":
        result = simpleCalculator(int(number[0]), int(number[2])).multiply()
        print(f"Result {result}")

except (ValueError, IndexError):
    print("Example Format: 1 + 2")
