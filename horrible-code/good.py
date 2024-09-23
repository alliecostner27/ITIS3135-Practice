class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def calculate(self):
        operations = {
            '1': ('add', self.add),
            '2': ('subtract', self.subtract),
            '3': ('multiply', self.multiply)
        }

        print("1. add\n2. subtract\n3. multiply")
        choice = input("Enter your choice (1/2/3): ")

        if choice in operations:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                operation_name, operation_func = operations[choice]
                result = operation_func(num1, num2)
                print(f"{num1} {operation_name} {num2} = {result}")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    calculator = Calculator()
    calculator.calculate()


        
    