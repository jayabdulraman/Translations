# Your challenge is to write a program that will take a text message and translate
# it into words your grandparents could understand. For example:
# So funny LOL ROTFL
# becomes
# So funny laughing out loud rolling on the floor laughing
# For this scenario we will start with a file that lists all the text message abbreviations and the translations
import fileinput

def mainFunction():
    """
    Function that takes an input with abbreviations and output a translated result
    """

    print("Enter Message")
    message = input("> ")

    messageWords = message.split()

    Transfilename = "Translations.txt"

    try:
        myFile = open(Transfilename)

        allAbbrevation, allTranslation = dictionaryList(Transfilename)

        translatedMessage = compare(messageWords, allAbbrevation, allTranslation)

        print('\n' + translatedMessage)
    except IOError:
        print("could not locate the file " + Transfilename)
        print("Could not translate message, file containing translation terms could not be located.")


def dictionaryList(fileName):
    """Function that takes an input, saves it into two dictionary lists, one for abbreviation and the other for
     translation"""

    allAbbreviation = []
    allTranslation = []

    myFile = open(fileName)

    for line in iter(myFile):

        wordsInTheLine = line.split()

        allAbbreviation.append(wordsInTheLine[0])

        translation = " "

        numOfWords = len(wordsInTheLine)

        for x in range(2, numOfWords):

            translation = translation + wordsInTheLine[x] + " "

        allTranslation.append(translation)

    return allAbbreviation, allTranslation


def compare(messageWords, allAbbreviation, allTranslation):
    """Function that compares the input message in the abbreviation with the translated list in the translation
    to give a final translated output"""
    finalMessage = ""

    # Step 3 d) Create a loop that will execute once for each word in our list of words in the text message
    for wordPosition in range(0, len(messageWords)):
        # Fetch the next word from our list of words in the text message
        currentWord = messageWords[wordPosition]

        try:
            # 3 d) search the abbreviation list for the current word
            matchPosition = allAbbreviation.index(currentWord.upper())

            # 3 e) If you find a match get the translation from the list of definitions
            finalMessage = finalMessage + " " + allTranslation[matchPosition] + '\n'
        except:
            # If no match is found by the index() search an exception is raised, which means no match was found
            # If no match was found just display the original word in the final message
            finalMessage = finalMessage + " " + currentWord

    return finalMessage


mainFunction()







