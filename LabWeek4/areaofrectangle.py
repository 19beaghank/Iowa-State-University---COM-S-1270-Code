#Kevin Beaghan  2/14/2025
#Lab A Week 4 - Converting Week 3 Code using functions

def areaofrectangle(b,h):
    area = b*h
    return area

def main():
    base = float(input("What is the length of the rectangles base?"))
    height = float(input("What is the rectangles height?"))
    area = areaofrectangle(base, height)
    print(f"The area of your rectangle is {area}.")

if __name__ == "__main__":
    main()