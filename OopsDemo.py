#classes are user defined blueprint or prototype
#sum, multiplication, addition, constant values
#methods, class variables, instance variables, constructor etc.
#objects for your classes
#variables assigned inside constructor is called instance variable
#functions inside class is called methods
#self keyword is mandatory if you declared method inside the class
# self keyword is mandatory for calling variable names into method
#instance and class variables have whole different purpose
#constructor name should be __init__
#new keyword is not required when you create object


class Calculator:
    num = 100 #class variable
    #default constructor
    def __init__(self, a, b):
        self.firstNumber= a #instance variable
        self.secondNumber= b #instance variable
        print(("I am called automatically when object is created"))

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(2, 3) #syntax to create objects in python
obj.getData()
print(obj.Summation())

obj1 = Calculator(4,5) #syntax to create objects in python
obj1.getData()
print(obj1.Summation())

