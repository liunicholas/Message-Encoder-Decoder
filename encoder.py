import random
import string

def encode(msg):
    # randCharList = list(string.ascii_lowercase) + (list(string.ascii_uppercase))
    randCharList = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}~")
    #amount of fake letters changes every time
    encodeLength = random.randrange(50,70)
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

def main():

    msg = ""
    efile = open("msg.txt", 'r')
    for line in efile:
        msg += line
    efile.close()

    encodedMsg, secretChar = encode(msg)

    print("\n%s" % encodedMsg)
    print("Secret character: %s\n" % secretChar)

main()
