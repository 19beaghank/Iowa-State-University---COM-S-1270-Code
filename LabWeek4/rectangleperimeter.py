#Kevin Beaghan  2/14/2025
#Lab A Week 4 - Converting Week 3 Code using functions

def rectangleperimeter(l,w):
    perimeter = 2*(l+w)
    return perimeter

def main():
    length = float(input("What is the rectangles length?"))
    width = float(input("What is the rectangles width?"))
    perimeter =     rectangleperimeter(length,width)
    print(f"The perimeter of your rectangle is {perimeter}.")

if __name__ == "__main__":
    main()