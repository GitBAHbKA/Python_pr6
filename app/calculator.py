import math
import random


class Calculator:
   def __init__(self, a, b):
       self.a = a
       self.b = b


   def add(self):
       return self.a + self.b


   def subtract(self):
       return self.a - self.b


   def multiply(self):
       return self.a * self.b


   def divide(self):
       return self.a / self.b


   def power(self):
       return math.pow(self.a, self.b)


   @staticmethod
   def random_number(a, b):
       return random.randint(min(a, b), max(a, b))