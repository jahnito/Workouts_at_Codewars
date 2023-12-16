'''
https://www.codewars.com/kata/53f1015fa9fe02cbda00111a

Color Ghost

Create a class Ghost

Ghost objects are instantiated without any arguments.

Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated

ghost = Ghost()
ghost.color  #=> "white" or "yellow" or "purple" or "red"
'''
from random import choice


class Ghost:
    def __init__(self):
        self.color = choice(["white", "yellow", "purple", "red"])
