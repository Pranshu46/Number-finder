def countWordsFromFile():
    fileName = input("enter the file name :-")

    NumberOfWords = 0
    file = open(fileName,'r')

    for line in file :
        words = line.split()
        NumberOfWords = NumberOfWords+len(words)

    print(NumberOfWords)

countWordsFromFile()