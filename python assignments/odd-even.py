class Number:
    def __init__(self, number):
        self.number = number

    def check_even_odd(self):
        if self.number % 2 == 0:
            print(self.number, "is Even.")
        else:
            print(self.number, "is Odd.")


num = int(input("Enter a number: "))
obj = Number(num)
obj.check_even_odd()
