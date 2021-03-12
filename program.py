from random import shuffle

# Function which, when given a string, scrambles each word and returns an output. 
# Words are defined as non-space characters separated by spaces
def scrambleWords(phrase):
    output = ""
    start = 0
    end = 0
    
    # For each found word, scramble it and add it to the output
    while(end!=len(phrase)):
        end=(phrase.find(" ",start))      
        if(end==-1):
            end = len(phrase)
        word = phrase[start:end]
        # convert word to list, shuffle list, join list back together, add to output
        wordList = list(word)
        shuffle(wordList)
        shuffledWord = ''.join(wordList)
        output= output + shuffledWord
        # Next iteration should start from the end
        start = end
        # For each space, add a space to the output
        while(start<len(phrase) and phrase[start]==" "):
            output+=" "
            start+=1
        
    return output

name = input("What is your name? ")


# This can change later, depending on what our program actually does

#TODO do something to the input

print("Hello, "+name)
inputString = input("Enter text to be scrambled: ")
print("\nHere are 5 ways to scramble those words:\n")


for x in range(5):
    print(scrambleWords(inputString))
