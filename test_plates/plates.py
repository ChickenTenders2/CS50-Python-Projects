import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not 2 <= len(s) <= 6:
        return False
    if not s[0:2].isalpha():
        return False
    if any(char in string.punctuation for char in s):
        return False

    first_digit = None
    for i, char, in enumerate(s):
        if char.isdigit():
            first_digit = i
            break

    if first_digit is not None:
        if s[first_digit] == "0":
            return False
        if not s[first_digit:].isdigit():
            return False
        if not s[:first_digit].isalpha():
            return False
    return True

if __name__ == "__main__":
    main()
