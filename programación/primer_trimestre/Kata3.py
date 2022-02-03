#https://www.codewars.com/kata/565b9d6f8139573819000056/train/python

"""
You have managed to intercept an important message and you are trying to read it.

You realise that the message has been encoded and can be decoded by switching each letter with a corresponding letter.

You also notice that each letter is paired with the letter that it coincides with when the alphabet is reversed.

For example: "a" is encoded with "z", "b" with "y", "c" with "x", etc

You read the first sentence:

"r slkv mlylwb wvxlwvh gsrh nvhhztv"
After a few minutes you manage to decode it:

"i hope nobody decodes this message"
Create a function that will instantly decode any of these messages

You can assume no punctuation or capitals, only lower case letters, but remember spaces!
"""


def decode(message):
    alfabeto = ['a','b','c','d','e','f,','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    inverso = alfabeto[::-1]
    traduccion = ''

    for caracter in message:
        if caracter.isalpha():
            posicion = alfabeto.index(caracter)
            traduccion += inverso[posicion]
        else:
            traduccion += caracter
    return traduccion
