'''
https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python



Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
Examples

"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"

Strings
Fundamentals


'elbuod decaps sdrow' should equal 'elbuod  decaps  sdrow'

'''


# def reverse_words(text: str) -> str:
#     conversation = []
#     char = None
#     elem = ''

#     for i in text:
#         if i == ' ' and char == ' ':
#             elem += i
#             char = i
#         elif i == ' ' and char != ' ':
#             conversation.append(elem)
#             elem = i
#             char = i
#         elif i != ' ' and char != ' ':
#             elem += i
#             char = i
#         elif i != ' ' and char == ' ':
#             conversation.append(elem)
#             elem = i
#             char = i
#     conversation.append(elem)
#     result = []
#     for i in conversation:
#         result.append(i[::-1])
#     return ''.join(result)


def reverse_words(text: str) -> str:
    return ' '.join(i[::-1] for i in text.split(' '))


if __name__ == '__main__':
    print(reverse_words('apple  huaple   teresa  reset'))
