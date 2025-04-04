import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    def new_format(time):
        match = re.match(r"(\d{1,2})(:\d{2})? ([APM]{2})", time)
        if not match:
            raise ValueError("Invalid Input")
        hour = int(match.group(1))
        minute = match.group(2)
        if minute:
            minute = int(minute[1:])
            if minute >= 60:
                raise ValueError("Invalid Input")
            minute = f":{minute:02d}"
        else:
            minute = ":00"
        period = match.group(3)

        if period == "AM":
            if hour == 12:
                hour = 0
        elif period == "PM":
            if hour != 12:
                hour += 12
        return f"{hour:02d}{minute}"

    try:
        if matches := re.search(r"^(\d{1,2}(:\d{2})? [APM]{2}) to (\d{1,2}(:\d{2})? [APM]{2})$", s):
            start = new_format(matches.group(1).strip())
            end = new_format(matches.group(3).strip())
            return f"{start} to {end}"
        else:
            raise ValueError("Invalid Input")
    except ValueError:
        raise ValueError("Invalid Input")

if __name__ == "__main__":
    main()
