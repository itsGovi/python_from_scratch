class BasicCalculator:
    def __init__(self):
        self.operations = ['add', 'sub', 'div', 'multi']
        while True:
            self.operation_called = input("What function do you wanna perform: ").lower()
            if self.operation_called == 'add':
                self.addition()
            elif self.operation_called == 'sub':
                self.subtraction()
            elif self.operation_called == 'multi':
                self.multiplication()
            elif self.operation_called == 'div':
                self.division()
            if self.operation_called == 'quit'.lower() or self.operation_called == 'exit'.lower(): # if you leave it with just or 'exit' it will take any value that not part of operations as singal to `break()`
                break

    def addition(self):
        if self.operation_called == 'add' and self.operation_called in self.operations:
            numbers = input("Give 2 numbers to add (seperated with ','): ")
            try:
                (x, y) = map(float, numbers.split(','))
                result = x + y
                print(f"The value of added no.'s is: {result}")
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a comma.")

    def subtraction(self):
        if self.operation_called == 'sub' and self.operation_called in self.operations:
            numbers = input("Give 2 no.'s to subtract: ")
            try:
                (x, y) = map(float, numbers.split(','))
                result = x - y
                print(f"The value of subtracted no.'s is: {result}")
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a comma.")
    
    def multiplication(self):
        if self.operation_called == 'multi' and self.operation_called in self.operations:
            numbers = input("Give 2 no's to multiply: ")
            try:
                (x, y) = map(float, numbers.split(','))
                result = x * y
                print(f"The value of multiplied no.'s is: {result}")
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a comma.")
    
    def division(self):
        if self.operation_called == 'div' and self.operation_called in self.operations:
            numbers = input("Give 2 no.'s to divide: ")
            try:
                (x, y) = map(float, numbers.split(','))
                result = x / y
                print(f"The value of divided no.'s is: {result}")
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a comma.")

calculator = BasicCalculator()


# Version 2
class BasicCalculator:
    def __init__(self):
        while True:
            self.operation_called = input("What calculation do you wanna perform: ")
            if self.operation_called == 'add':
                self.addition()
            elif self.operation_called == 'sub':
                self.subtract()
            elif self.operation_called == 'multiply':
                self.multiply()
            elif self.operation_called == 'div':
                self.division()
            elif self.operation_called == 'quit'.lower() or  self.operation_called == 'exit'.lower():
                break

    def addition(self):
        if self.operation_called == 'add':
            try:
                numbers = input("Give 2 no's to add: ")
                (x, y) = map(float, numbers.split(','))
                result = x + y
                print(f"The value of adding {x} and {y} is: {result}")
            except ValueError:
                print("The values need to be a number!")
    def subtract(self):
        if self.operation_called == 'sub':
            try:
                numbers = input("Give 2 no's to subtract: ")
                (x, y) = map(float, numbers.split(','))
                result = x - y
                print(f"The value of subtracting {x} and {y} is: {result}")
            except ValueError:
                print("The values need to be a number!")
    
    def multiply(self):
        if self.operation_called == 'multiply':
            try:
                numbers = input("Give 2 no's to multiply: ")
                (x, y) = map(float, numbers.split(','))
                result = x * y
                print(f"The value of multiplying {x} and {y} is: {result}")
            except ValueError:
                print("The values need to be a number!")
    
    def division(self):
        if self.operation_called == 'div':
            try:
                numbers = input("Give 2 no's to divide: ")
                (x, y) = map(float, numbers.split(','))
                result = x / y
                print(f"The value of dividing {x} and {y} is: {result}")
            except ValueError:
                print("The values need to be a number!")


calculator = BasicCalculator()