'''
https://www.codewars.com/kata/59ea2a532a7accf2510000ce

The story of the famous Disney-Pixar animated movie "Up" is based on the main character Carl Fredricksen journey in his home equipped with balloons.

But can this happen for real? What kind of objects can you lift with helium balloons? How many balloons do you need?

In this kata you will create a class

Journey(object, crew, balloons)

so anyone can create objects like

var gravityFalls = new Journey(house, 2, 20622)

which means starting a new journey to Gravity Falls in a house with 2 members of crew (Carl and Russel).

But is this journey possible? Will the house float? Is it enough to have 20622 helium balloons (the number used by Pixar animators in liftoff scene)?

Your Journey class should have a public method isPossible() that returns true or false based on these rules:

1). Every object (dictionary in Python) passed to Journey will have its weight property like

var house = {"weight": 45000};

(we will use metric system in this kata, 45 000 kg is about 100 000 pounds).

2). Each member of the crew weighs 80 kg.

3). We use regular sized party balloons filled with helium. Each balloon lifts 4.8 grams + its own weight.

Can you lift a tiny 95 kg(~200 pound) push cart with 50 balloons like in one of the starting scenes of the movie?

Can one balloon actually carry a message on a single letter-sized paper sheet sent by Carl to his dying wife Ellie in the other scene?

Can the story I heard about man flying in his lawn chair equipped with 1000 balloons be true?

Your coding mastery will reveal answers to these and many other important questions in the tests. Let the journey begin!
'''

class Journey:
    def __init__(self, jorn: dict, crew: int, balloons: int):
        self.jorn_box = jorn.get('weight', 0) * 1000
        self.crew = crew
        self.balloons = balloons
        self.weight_member = 80000
        self.one_lift_power = 4.8

    def isPossible(self):
        full_weight = self.crew * self.weight_member + self.jorn_box
        full_power = self.one_lift_power * self.balloons
        return full_power > full_weight


if __name__ == '__main__':
    letter = {'weight': 0.004536}
    house = {'weight': 45000}
    pushCart = {'weight': 95}
    lawnChair = {'weight': 5}

    flyingCart = Journey(pushCart, 0, 50)
    loveOfMyLife = Journey(letter, 0, 1)
    gravityFalls = Journey(house, 2, 20622)

    print(flyingCart.isPossible())
    print(loveOfMyLife.isPossible())
    print(gravityFalls.isPossible())
