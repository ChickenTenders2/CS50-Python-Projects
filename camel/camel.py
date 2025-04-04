camel_case = input("camelCase: ")
chars = [char for char in camel_case]

for char_num in range(len(chars)):
    if chars[char_num].isupper():
        chars[char_num] = chars[char_num].lower()
        chars.insert(char_num, "_")

print("".join(chars))
