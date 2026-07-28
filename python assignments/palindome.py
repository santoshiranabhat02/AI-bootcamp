class Palindrome:
    def __init__(self, text):
        self.text = text

    def check_palindrome(self):
        if self.text == self.text[::-1]:
            print(self.text, "is a Palindrome.")
        else:
            print(self.text, "is not a Palindrome.")


word = input("Enter a word: ")
obj = Palindrome(word)
obj.check_palindrome()
