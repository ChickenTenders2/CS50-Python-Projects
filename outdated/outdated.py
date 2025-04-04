months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def month_number(month):
    try:
        return months.index(month) + 1
    except ValueError:
        pass

while True:
    try:
        date = input("Date: ").strip()
        if "/" in date:
            details = date.split("/")
            month_num, day, year = details
            if not (1 <= int(month_num) <= 12):
                continue
            if not (1 <= int(day) <= 31):
                continue
            print(f"{year}-{int(month_num):02d}-{int(day):02d}")
            break
        else:
            if "," in date and date[0].isalpha():
                details = date.replace(",","").split()
                month_name, day, year = details
                month_num = month_number(month_name)
                if not (1 <= int(month_num) <= 12):
                    continue
                if not (1 <= int(day) <= 31):
                    continue
                print(f"{year}-{int(month_num):02d}-{int(day):02d}")
                break
            else:
                continue
    except (ValueError, EOFError):
        continue

