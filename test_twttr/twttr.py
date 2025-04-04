def main():
    word = input("Input: ")
    print(shorten(word))

def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    chars = [char for char in word]
    for char in chars[:]:
        if char in vowels:
            chars.remove(char)
    return "".join(chars)

if __name__ == "__main__":
    main()
