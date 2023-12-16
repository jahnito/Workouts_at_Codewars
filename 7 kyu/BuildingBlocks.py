'''
https://www.codewars.com/kata/55b75fcf67e558d3750000a3/train/python

Write a class Block that creates a block (Duh..)
Requirements

The constructor should take an array as an argument, this will contain 3 integers of the form [width, length, height] from which the Block should be created.

Define these methods:

`get_width()` return the width of the `Block`

`get_length()` return the length of the `Block`

`get_height()` return the height of the `Block`

`get_volume()` return the volume of the `Block`

`get_surface_area()` return the surface area of the `Block`

Examples

    b = Block([2,4,6]) -> create a `Block` object with a width of `2` a length of `4` and a height of `6`
    
    b.get_width() -> return 2
    
    b.get_length() -> return 4
    
    b.get_height() -> return 6
    
    b.get_volume() -> return 48
    
    b.get_surface_area() -> return 88

Note: no error checking is needed

Any feedback would be much appreciated
'''

class Block:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def get_width(self):
        return self.dimensions[0]

    def get_length(self):
        return self.dimensions[1]

    def get_height(self):
        return self.dimensions[2]

    def get_volume(self):
        res = 1
        for i in self.dimensions:
            res *= i
        return res

    def get_surface_area(self):
        res = 0
        for x, y in ([1,2], [1,3], [2,3]):
            res += self.dimensions[x-1] * self.dimensions[y-1] * 2
        return res


if __name__ == '__main__':
    block = Block([2,2,2])
    print(block.get_width())
    print(block.get_lenght())
    print(block.get_height())
    print(block.get_volume())
    print(block.get_surface_area())
