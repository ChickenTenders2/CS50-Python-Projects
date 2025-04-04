import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if matches := re.search(r'^<iframe.*?src="(https?)://(www\.)?(youtu)(be)\.com/embed(/xvFZjo5PgG0)".*?></iframe>$', s, re.IGNORECASE):
        protocol = matches.group(1)
        if protocol == "http":
            protocol += "s"
        return protocol + "://" + matches.group(3) + "." + matches.group(4) + matches.group(5)

if __name__ == "__main__":
    main()
