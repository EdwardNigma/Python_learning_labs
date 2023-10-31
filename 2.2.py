
#from typing import Any


class Snow:
    def __init__(self, x):
        self.snowflake = x

    def __call__(self, number):
        self.snowflake = number
    
    def __add__(self, n):
        return Snow(self.snowflake + n)
    
    def __sub__(self, n):
        return Snow(self.snowflake - n)
    
    def __mul__(self, n):
        return Snow(self.snowflake * n)
    
    def __truediv__(self, n):
        return Snow(self.snowflake // n)
    
    def makeSnow(self, number_in_row):
        printed_snowflakes_number = 0
        for i in range(int(self.snowflake // number_in_row) + 1):
            if (i != (int(self.snowflake // number_in_row))):
                printed_snowflakes_number += number_in_row
                print(number_in_row * "*")
            else:
                print((self.snowflake - printed_snowflakes_number) * "*")


snowflake_1 = Snow(14)
snowflake_1(18)
x = snowflake_1 / 2
print(x.snowflake)
Snow.makeSnow(x, 6)