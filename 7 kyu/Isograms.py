'''
https://www.codewars.com/kata/54ba84be607a92aa900000f1

An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false
'''


def is_isogram(string):
    '''
    Побуквенно пробегаем по строке и проверяем количество букв,
    если больше 1 то возвращаем False
    '''
    for i in string.lower():
        if string.lower().count(i) != 1:
            return False
    return True

word = input()
print(is_isogram(word))
