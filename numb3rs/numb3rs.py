import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if matches := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        return all(0 <= int(octet) <= 255 for octet in matches.groups()) #octet represents each # in #.#.#.#
    return False

if __name__ == "__main__":
    main()
