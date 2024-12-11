class ConversionOfUnits:
    def __init__(self):
        self.conversion_types = ['temperature', 'weight', 'distance']
        self.units = {
            'temperature': ['Celsius', 'Fahrenheit', 'Kelvin'],
            'weight': ['Kilograms', 'Pounds', 'Ounces'],
            'distance': ['Meters', 'Kilometers', 'Miles']
        }

    def run(self):
        ask_input = input("What conversion metrics do yo wanna use:\n1. Temperature\n2. Weight\n3. Distance")
        while True:    
            if ask_input == ['1', '2', '3', 'exit', 'quit']:
                if ask_input == '1':
                    self.temperature_conversion()
                elif ask_input == '2':
                    self.weight_conversion()
                elif ask_input == '3':
                    self.distance_conversion()
                elif ask_input in ['exit', 'quit']:
                    print("Exiting the program...")
                    break
            else:
                print("Please enter the given serial no. of the type of conversion and nothing else")
        
    def temperature_conversion(self):
