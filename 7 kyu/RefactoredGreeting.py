'''
https://www.codewars.com/kata/5121303128ef4b495f000001

The following code could use a bit of object-oriented artistry. While it's a simple method and works just fine as it is, in a larger system it's best to organize methods into classes/objects. (Or, at least, something similar depending on your language)

Refactor the following code so that it belongs to a Person class/object. Each Person instance will have a greet method. The Person instance should be instantiated with a name so that it no longer has to be passed into each greet method call.

Here is how the final refactored code would be used:

joe = Person('Joe')
joe.greet('Kate') # should return 'Hello Kate, my name is Joe'
joe.name          # should == 'Joe'
'''

# Old code
# def greet(my_name, your_name):
#     return "Hello %s, my name is %s" % (your_name, my_name)

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self, greet_name):
        return "Hello %s, my name is %s" % (greet_name, self.name)

if __name__ == '__main__':
    joe = Person('Joe')
    print(joe.greet('Kate'))
