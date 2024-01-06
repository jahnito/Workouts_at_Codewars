'''
https://www.codewars.com/kata/55c1d030da313ed05100005d


Now that we have a Block let's move on to something slightly more complex: a Sphere.
Arguments for the constructor

radius -> integer or float (do not round it)
mass -> integer or float (do not round it)

Methods to be defined

get_radius()       =>  radius of the Sphere (do not round it)
get_mass()         =>  mass of the Sphere (do not round it)
get_volume()       =>  volume of the Sphere (rounded to 5 place after the decimal)
get_surface_area() =>  surface area of the Sphere (rounded to 5 place after the decimal)
get_density()      =>  density of the Sphere (rounded to 5 place after the decimal)

Example

ball = Sphere(2,50)
ball.get_radius() ->       2
ball.get_mass() ->         50
ball.get_volume() ->       33.51032
ball.get_surface_area() -> 50.26548
ball.get_density() ->      1.49208

Any feedback would be much appreciated
'''


from math import pi


class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round((pi * self.radius ** 3) * 4 / 3, 5)

    def get_surface_area(self):
        return round(pi * 4 * self.radius **2, 5)

    def get_density(self):
        return round(self.mass / self.get_volume(), 5)


if __name__ == '__main__':
    s1 = Sphere(2, 50)
    print(s1.get_volume())
    print(s1.get_surface_area())
    print(s1.get_density())
