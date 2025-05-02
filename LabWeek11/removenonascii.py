#Kevin Beaghan 3/31/2025
#Week 11 Lab - Opening a file and removing any Non ASCII characters

def final_file(file, clean):
    newFile = file.split('.')[0] + "_clean.txt"
    with open(newFile, 'w', encoding="utf8") as f:
        f.write(clean)
    print(f"Cleaned content written to {newFile}")

def removeNonASCII(text):
    clean = ""
    for char in text:
        if ord(char) < 128:
            clean += char
    return clean

def prep_file(file):
    with open(file, 'r',encoding="utf8") as f:
        text = f.read()
    return text

def main():
    file = input("Please enter the file name:")
    text = prep_file(file)
    clean = removeNonASCII(text)
    final_file(file, clean)

if __name__ == "__main__":
    main()