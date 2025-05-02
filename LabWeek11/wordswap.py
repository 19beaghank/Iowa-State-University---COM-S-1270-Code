#Kevin Beaghan 3/31/2025
#Week 11 Lab - Taking inputs into a dictionary and randomly swapping words unign keys and randomly chosen values

import random

def map(words):
    wordMap = {}
    for word in set(words):
        wordMap[word] = random.choice(words)
    return wordMap

def main():
    sentence = input("Enter a sentence:")
    words = sentence.split()
    wordMap = map(words)
    print(f"Word Map: {wordMap}")
    newWords = [wordMap[word] for word in words]
    new = " ".join(newWords)
    print(f"New Sentence: {new}")

if __name__ == "__main__":
    main()