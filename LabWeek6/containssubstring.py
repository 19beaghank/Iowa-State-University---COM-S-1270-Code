#Kevin Beaghan  2/28/2025
#Week 6 Lab - 

# https://docs.python.org/3/library/stdtypes.html
# accessed 3/2/2025

def containsSubstring(h,n):
    index = h.find(n)
    if index == -1:
        print(f"The string '{h}' did not contain the sub-string '{n}'")
    else:
        print(f"The string '{h}' contained the sub-string '{n}' at index {index}")

def main():
    haystack = input("Input a sting:")
    needle = input("Input another sting:")
    containsSubstring(haystack, needle)

if __name__ == "__main__":
    main()