'''
Count the smiley faces
https://www.codewars.com/kata/583203e6eb35d7980400002a/train/python


Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

Rules for a smiling face:

    Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
    A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
    Every smiling face must have a smiling mouth that should be marked with either ) or D

No additional characters are allowed except for those mentioned.

Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]
Example

countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;

Note

In case of an empty array return 0. You will not be tested with invalid input (input will always be an array). Order of the face (eyes, nose, mouth) elements will always be the same.
'''

def count_smileys(arr):
    c = 0
    valid_f0 = [':', ';']
    valid_f1 = ['-', '~']
    valid_f2 = [')', 'D']

    for i in arr:
        if len(i) == 2 and i[0] in valid_f0 and i[1] in valid_f2:
            c += 1
        elif len(i) == 3 and i[0] in valid_f0 and i[1] in valid_f1 and i[2] in valid_f2:
            c += 1
    return c


if __name__ == '__main__':
    for i in ([], [':D',':~)',';~D',':)'], [':)',':(',':D',':O',':;'], [';]', ':[', ';*', ':$', ';-D']):
        print(count_smileys(i))
