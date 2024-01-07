'''
https://www.codewars.com/kata/5be1a950d2055d589500005b/train/python

In this kata you will try to recreate a simple code-breaking game. It is called "Bulls and Cows". The rules are quite simple:

The computer generates a secret number consisting of 4 distinct digits. Then the player, in 8 turns, tries to guess the number. As a result he receives from the computer the number of matches. If the matching digits are in their right positions, they are "bulls", if in different positions, they are "cows".

To implement this you will use:

1)a constructor (int) - initiates the game, receives a number and then sets it as the secret number.

2)and a function "compare with (int)" - compares the given and the secret numbers and then returns a String formated as "X bull/bulls and Y cow/cows".

However, there are some notes:

1)if the given number matches the secret number instead of returning "4 bulls and 0 cows", return "You win!". Any next attempts to play the game (even with invalid numbers) should return "You already won!"

2)if the amount of turns in this game is more than 8 (invalid turns are not counted) the returned String should be "Sorry, you're out of turns!".

3)After checking the turns you should validate the given number. If it does not correspond to the conditions you should throw an exception :


Game starts with the secret number 9041

compare with : 8091
result : "2 bulls and 1 cow" # The bulls are "0" and "1", the cow is "9"

compare with : -15555
result : Exception # A number should be positive and contain 4 distinct digits. 
                   # This turn is not counted
                   
compare with : 8237
result : "0 bulls and 0 cows"

compare with : 9041
result : "You win!"

# new comparations (even with invalid numbers) will result in : "You already won!"
# the same logic applies to being out of turns
'''
from random import randint


class BullsAndCows:
    def __init__(self, n):
        if not self.check_uniq(n):
            raise ValueError
        self.num = n
        self.win = False
        self.attempts = 8

    def compare_with(self, n):
        if self.check_win():
            return 'You already won!'
        if self.check_attempts():
            return 'Sorry, you\'re out of turns!'
        if not self.check_uniq(n):
            raise ValueError
        if n == self.num:
            self.win = True
            return 'You win!'
        bulls = self.check_bulls(n)
        cows = self.check_cows(n)
        b = 'bulls' if bulls != 1 else 'bull'
        c = 'cows' if cows != 1 else 'cow'
        self.attempts -= 1
        return f'{bulls} {b} and {cows} {c}'


    def check_uniq(self, n):
        if 1000 < n < 10000 and len(set(str(n))) == 4:
            return True
        else:
            return False

    def check_win(self):
        if self.win:
            return True
        else:
            return False

    def check_attempts(self):
        if self.attempts == 0:
            return True
        else:
            return False

    def check_bulls(self, n):
        res = 0
        secret_num, num = str(self.num), str(n)
        for i in range(4):
            if secret_num[i] == num[i]:
                res += 1
        return res

    def check_cows(self, n):
        res = 0
        secret_num, num = str(self.num), str(n)
        for i in range(4):
            if secret_num[i] != num[i] and num[i] in secret_num:
                res += 1
        return res


if __name__ == '__main__':
    bac = BullsAndCows(4321)
    for i in range(9):
        print(bac.compare_with(4031))
