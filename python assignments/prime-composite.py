class Number:
    def __init__(self, number):
        self.number = number

    def check_prime_composite(self):
        if self.number <= 1:
            print("Neither Prime nor Composite.")
            return

        count = 0

        for i in range(1, self.number + 1):
            if self.number % i == 0:
                count += 1

        if count == 2:
            print(self.number, "is Prime.")
        else:
            print(self.number, "is Composite.")


num = int(input("Enter a number: "))
obj = Number(num)
obj.check_prime_composite()
