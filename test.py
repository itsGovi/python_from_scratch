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