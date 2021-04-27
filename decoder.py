import string

# randCharList = list(string.ascii_lowercase) + (list(string.ascii_uppercase))
randCharList = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}~ ")

def decode(encodedMsg, secretChar):

    charsInMsg = 0
    decodedMsg = ""

    for char in encodedMsg:
        if char == secretChar:
            charsInMsg += 1

    # if charsInMsg == 0:
    #     return "NA"

    fakeLetters = int(len(encodedMsg) / charsInMsg)
    # print(fakeLetters)

    for i in range(1, charsInMsg + 1):
        decodedMsg += encodedMsg[fakeLetters * i - 1]

    return decodedMsg

def reverseShift(encodedMsg, shiftLength):
    newEncodedMsg = ""
    for i in range(len(encodedMsg)):
        currentIndex = randCharList.index(encodedMsg[i])
        # print(shiftLength)
        shiftedIndex = currentIndex - int(shiftLength)
        # newIndex = shiftedIndex % len(randCharList)
        newEncodedMsg+=randCharList[shiftedIndex]

    return encodedMsg

def main():
    encodedMsg = ""
    efile = open("msg.txt", 'r')
    for line in efile:
        encodedMsg += line
    efile.close()

    key = input("enter key: ")

    # for i in range(len(randCharList)):
    #     secretChar = randCharList[i]
    #     decodedMsg = decode(encodedMsg, secretChar)
    #     print(randCharList[i] + " : " + decodedMsg)
    for i in range(len(key)-1,0,-2):
        #key[i] is shift length
        encodedMsg = reverseShift(encodedMsg, key[i])
        # print(f"after shift: {encodedMsg}")
        #key[i-1] is secretChar
        encodedMsg = decode(encodedMsg, key[i-1])
        # print(f"after decode: {encodedMsg}")

    print("\n"+encodedMsg)

main()
