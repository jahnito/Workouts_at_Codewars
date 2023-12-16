'''
https://www.codewars.com/kata/55a144eff5124e546400005a

Classy Classes

Basic Classes, this kata is mainly aimed at the new JS ES6 Update introducing classes
Task

Your task is to complete this Class, the Person class has been created. You must fill in the Constructor method to accept a name as string and an age as number, complete the get Info property and getInfo method/Info getter which should return johns age is 34

Reference: https://docs.python.org/3/tutorial/classes.html
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f"{name}s age is {age}"

    def get_info(self):
        return self.info


if __name__ == '__main__':
    m1 = Person('john', 34)
    print(m1.get_info())
