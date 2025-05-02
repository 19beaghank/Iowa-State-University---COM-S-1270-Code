#Kevin Beaghan 3/31/2025
#Week 11 Lab - Using dictionaries and counts to find the number of times a word is used in a file

def outputAnalysis(count, file):
    newFile = file.split('.')[0] + "_analysis.txt"
    sort = sorted(count.keys())
    with open(newFile, 'w') as f:
        for key in sort:
            f.write(f"{key}: {count[key]}\n")

def analyzeBook(file):
    with open(file, 'r',encoding="utf8") as f:
        count = {}
        for line in f:
            for word in line.split():
                word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
                word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
                word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
                word = word.replace(']', '').replace(';', '')
                word = word.lower()
                if word.isalpha():
                    if word in count:
                        count[word] = count[word] + 1
                    else:
                        count[word] = 1
        keys = list(count.keys())
        keys.sort()
        out = open('alice_words.txt', 'w')
        for word in keys:
            out.write(word + " " + str(count[word]))
            out.write('\n')
    return count

def main():
    file = input("Please enter the file name:")
    count = analyzeBook(file)
    outputAnalysis(count, file)

if __name__ == "__main__":
    main()