'''
https://www.codewars.com/kata/57c9313cf8392dd5480000fa/train/python

Description

In AD 2050, human beings finally found a planet in the distant XY constellation, which is very suitable for human survival. Many spacecraft from the earth to the distant planet, the star immigrants began...

Nearly 10 years later, Human civilization is built up in the new planet, they put the planet named "paradise" and they call themselves "new human beings".

They created their own language on the basis of the English alphabet and binary. That is to say, their text is expressed in binary, but only limited to letters, they still use punctuation and spaces in English.

They use some special rules:

    Their binary is the opposite of the "old human beings". That is to say, their 1 is equals to our 0 and their 0 is equals to our 1.

    They re-encode the English alphabet in the opposite order: "zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA", using binary 1 to 52. For example, z is 10, y is 01, x is 00, and so on.. Each letter ends with 2. See examples below:

old human beings: Hello world!
new human beings: 0100102(H)010012(e)00002(l)00002(l)00112(o)
                  0112(w)00112(o)01102(r)00002(l)010002(d)!

old human beings: I am new human beings.
new human beings: 0100112(I) 001012(a)00012(m) 00102(n)010012(e)0112(w)
                  011002(h)0012(u)00012(m)001012(a)00102(n) 
                  001102(b)010012(e)011012(i)00102(n)010112(g)01112(s).

Task

Complete two function encode and decode that can tranlate the words between "new human beings" and "old human beings".
Examples

encode("Hello world!") should return:
"0100102010012000020000200112 0112001120110200002010002!"

decode("0100102010012000020000200112 0112001120110200002010002!") 
should return: "Hello world!"

decode(encode("Hello world!")) should return "Hello world!"
'''

ABC = 'zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA'


def encode(s: str) -> str:
    def convert(let: str) -> str:
        if let in ABC:
            index = ABC.index(let)
            return ''.join(['0' if i == '1' else '1' for i in bin(index + 1)[2:]]) + '2'
        else:
            return let

    result = ''
    for i in s:
        result += convert(i)

    return result


def decode(s: str) -> str:
    def convert(inv_bin_let: str) -> int:
        a = ['0' if i == '1' else '1' for i in inv_bin_let]
        return ABC[int('0b' + ''.join(a), base=2) - 1]
    res = []
    k = ''
    for i in s:
        if i == '2':
            res.append(k)
            k = ''
        elif not i.isdigit() and (not k or not k.isdigit()):
            k += i
        elif i.isdigit() and (not k or k.isdigit()) and i != '2':
            k += i
        elif not i.isdigit() and k.isdigit():
            res.append(k)
            k = i
        elif i.isdigit() and not k.isdigit():
            res.append(k)
            k = i
    res.append(k)

    result = []
    for i in res:
        if i.isdigit():
            result.append(convert(i))
        else:
            result.append(i)

    return ''.join(result)


if __name__ == '__main__':
    print(decode('012?'))
    print(decode(''))
    print(encode('} IF T/Hja PxR&d  _LuC. Ir]C&. K^Vt=U! [S!zq|GJB; WPh?X\\K {W_NfA wV) HcglYMarOb _Z}|xLCk {-!l_HT _](Ca.'))
    print(encode('[p_rnm% %W  -G/ fyeiL $tI*^*IN@ I)p^[, Si}XFPo &#UF+gSk ?Rpe Ovu b-{j)vu. Ow {@-z p_j|{Sf+=u L}O([\\(aWX;'))
