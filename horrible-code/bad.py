class NumbFixer:
    def AD(self, x, y):
        return x + y

    def MINUS(self, x, y):
        return x - y

    def TIMESX(self, x, y):
        return x * y

    def calculate(self):
        print("1. AD")
        print("2. MINUS")
        print("3. TIMESX")

        choice = input("Enter choice(1/2/3): ")

        if choice in ['1', '2', '3']:
            try:
                num1 = float(input("Enter a numero: "))
                num2 = float(input("Enter second numero: "))

                if choice == '1':
                    print(f"{num1} + {num2} = {self.AD(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {self.MINUS(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {self.TIMESX(num1, num2)}")
            except ValueError:
                print("Invalid..enter numero values.")
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    fixer = NumbFixer()
    fixer.calculate()




    
    