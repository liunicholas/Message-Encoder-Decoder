import string

def decode(encodedMsg, secretChar):

    charsInMsg = 0
    decodedMsg = ""

    for char in encodedMsg:
        if char == secretChar:
            charsInMsg += 1

    if charsInMsg == 0:
        return "NA"

    fakeLetters = len(encodedMsg) / charsInMsg

    for i in range(1, charsInMsg + 1):
        decodedMsg += encodedMsg[fakeLetters * i - 1]

    return decodedMsg

def main():

    encodedMsg = ""
    efile = open("msg.txt", 'r')
    for line in efile:
        encodedMsg += line
    efile.close()

    # randCharList = list(string.ascii_lowercase) + (list(string.ascii_uppercase))
    randCharList = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}~ ")
    for i in range(len(randCharList)):
        secretChar = randCharList[i]
        decodedMsg = decode(encodedMsg, secretChar)
        print(randCharList[i] + " : " + decodedMsg)

main()
