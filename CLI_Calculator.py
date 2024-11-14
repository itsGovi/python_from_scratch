class BasicCalculator:
    def __init__(self):
        self.operations = ['add', 'sub', 'div', 'multi']
        self.operation_called = input("What function do you wanna perform: ").lower()
        if self.operation_called == 'add':
            self.addition()
        elif self.operation_called == 'sub':
            self.subtraction()
        elif self.operation_called == 'multi':
            self.multiplication()
        else:
            self.division()
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
            numbers = input("Give 2 numbers to subtract: ")
        try:
            (x, y) = map(float, numbers.split(','))
            result = x - y
            print(f"The value of subtracted no.'s is: {result}")
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a comma.")
    
    def multiplication(self):
        if self.operation_called == 'multi' and self.operation_called in self.operations:
            numbers = input("Give 2 numbers to multiply: ")
        try:
            (x, y) = map(float, numbers.split(','))
            result = x * y
            print(f"The value of multiplied no.'s is: {result}")
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a comma.")
    
    def division(self):
        if self.operation_called == 'div' and self.operation_called in self.operations:
            numbers = input("Give 2 no.'s to multiple: ")
        try:
            (x, y) = map(float, numbers.split(','))
            result = x / y
            print(f"The value of divided no.'s is: {result}")
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a comma.")

calculator = BasicCalculator()