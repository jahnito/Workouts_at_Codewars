'''
Find character

Description:

Give you a character matrix. Find out the character which has the smallest amount.
Arguments:

    matrix: A string that contains some letters. Each row is separated by "\n".

Results & Note:

    Returns the characters which has smallest amount, using string format.
    If more than one characters are found, sort them according to the order A-Za-z0-9.
    You can assume that there are at least two characters in the matrix.
    Please ignore the "\n" ;-)

Some Examples

matrix=
00000000
0000O000
00000000
00000000
00000000

result -> "O"

matrix=
mmmmmmmmmmmmm
mmmmmmmmmmmmm
mmmmmmmmmmmmm
mmmmmmmmmnmmm

result -> "n"

matrix=
AAAAAAAAAAA
AABBBBBBBBB
BCCCCCCCCDD
DDDDEEEEFFF

result -> "F"

matrix=
AAAAA
ABBBB
BCCCC
DDDDE
EEEEF
FFFFF

result -> "CD"

'''

mtrxs = ['''00000000
0000O000
00000000
00000000
00000000''',
'''mmmmmmmmmmmmm
mmmmmmmmmmmmm
mmmmmmmmmmmmm
mmmmmmmmmnmmm
''',
'''AAAAAAAAAAA
AABBBBBBBBB
BCCCCCCCCDD
DDDDEEEEFFF
''',
'''AAAAA
ABBBB
BCCCC
DDDDE
EEEEF
FFFFF
''',
'''3v652
1uwyt
v254v
t54tv
x45yx
s7x45
5402v
2x3xw
5w22v'''
]


def find_characters(matrix: str) -> str:
    def sortUP(s: str) -> str:
        return ''.join(sorted(filter(lambda x: x.isupper(), s)))

    def sortLOW(s: str) -> str:
        return ''.join(sorted(filter(lambda x: x.islower(), s)))

    def sortDIG(s: str) -> str:
        return ''.join(sorted(filter(lambda x: x.isdigit(), s)))

    def getline(s: str) -> str:
        res = {}
        for i in set(matrix.strip().replace('\n', '')):
            if (c := matrix.count(i)) in res:
                res[c] += i
            else:
                res[c] = i
        return res[min(res.keys())]

    line = getline(matrix)
    return sortUP(line) + sortLOW(line) + sortDIG(line)


if __name__ == '__main__':
    for i in mtrxs:
        print(find_characters(i))