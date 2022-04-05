#! /usr/bin/env python3

class Calculator:
       

    def __init__(self, x, y):
        #initialise
        self.x = x
        self.y = y
    
    def adder(self):
        #Add
        return self.x + self.y

    def subtractor(self):
        # minus
        return self.x - self.y

    def multiplier(self):
        # multiplier
        return self.x * self.y
    
    def divider(self):
        #divider
        return self.x / self.y

    def clear(self):
        # clear the value
        self.x = 0
        self.y = 0


def main():
    user_input_one  = input('one: ')
    user_input_two  = input('two: ')
    # Calculate
    calculator = Calculator(int(user_input_one), int(user_input_two))
    
    print(calculator.adder())
    print(calculator.subtractor())
    print(calculator.multiplier())
    print(calculator.divider())


    calculator.clear()


if __name__ == "__main__":
    main()
