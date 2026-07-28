class Factorial:
    def __init__(self, number):
        self.number = number

    def calculate(self):
        fact = 1

        for i in range(1, self.number + 1):
            fact *= i

        print("Factorial =", fact)


num = int(input("Enter a number: "))
obj = Factorial(num)
obj.calculate()
