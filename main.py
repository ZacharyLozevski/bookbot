def main():
    filePath = "./books/frankenstein.txt"

    text = readInFile(filePath)

    wordCount = getNumberOfWords(text)

    letterCountDict = getNumberOfLetters(text)

    letterCountList = convertToList(letterCountDict)
    
    letterCountList.sort(reverse=True, key=keyOfDict)

    generateBookReport(filePath, wordCount, letterCountList)

    return 0

def generateBookReport(path, numWords, lettersList):
    print(f"---- Book report of {path[2:]} ----")
    print(f"There was a total number of {numWords} words.\n")

    for item in lettersList:
        print(f"The letter {item['letter']} appeared {item['count']} amount of times")

    print(f"---- End of Book report ----")

def keyOfDict(userDict):
    return userDict["count"]

def convertToList (userDict):
    userList = []
    for letter, count in userDict.items():
        if letter.isalpha():
            userList.append({"letter": letter, "count": int(count)})
    return userList

def getNumberOfLetters(text):
    letterCount = {}
    for letter in text:
        letter = letter.lower()
        if letter in letterCount.keys():
            letterCount[letter] += 1
        else:
            letterCount[letter] = 1
    return letterCount

def getNumberOfWords(text):
    return (len(text.split()))
    
def readInFile(file):
    with open(file) as f:
        return f.read()

main()