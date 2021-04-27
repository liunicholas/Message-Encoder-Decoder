import random
import string

# randCharList = list(string.ascii_lowercase) + (list(string.ascii_uppercase))
randCharList = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}~")

def encode(msg):
    # randCharList = list(string.ascii_lowercase) + (list(string.ascii_uppercase))
    # randCharList = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}~")
    #amount of fake letters changes every time
    encodeLength = random.randrange(3,7)
    #letter changes evry time
    encodeChar = random.choice(randCharList)
    encodedMsg = ""
    for i in range(len(msg)):
        fakeLetterCount = 0
        #different spot for encodedChar each time
        encodeCharSpot = random.randrange(1, encodeLength - 1)

        while fakeLetterCount < encodeLength:
            if fakeLetterCount == encodeCharSpot and encodeChar != msg[i]:
                encodedMsg += encodeChar

            else:
                fakeLetter = random.choice(randCharList)
                while fakeLetter == encodeChar:
                    fakeLetter = random.choice(randCharList)
                encodedMsg += fakeLetter
            fakeLetterCount += 1

        encodedMsg += msg[i]

    return encodedMsg, encodeChar

def shiftCode(encodedMsg):
    shiftLength = random.randrange(0,10)
    newEncodedMsg = ""
    for i in range(len(encodedMsg)):
        currentIndex = randCharList.index(encodedMsg[i])
        shiftedIndex = currentIndex + shiftLength
        newIndex = shiftedIndex % len(randCharList)
        newEncodedMsg+=randCharList[newIndex]

    return encodedMsg, shiftLength

def main():
    encodedMsg = ""
    efile = open("msg.txt", 'r')
    for line in efile:
        encodedMsg += line
    efile.close()

    key = ""
    for i in range(3):
        encodedMsg, secretChar = encode(encodedMsg)
        key+=secretChar
        encodedMsg, secretShift = shiftCode(encodedMsg)
        key+=str(secretShift)

    print("\n%s" % encodedMsg)
    print("\nkey: %s\n" % key)

main()
