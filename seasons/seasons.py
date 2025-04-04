from datetime import date, datetime
import inflect
import sys

class Age:
    def __init__(self, birthdate):
        self.birthdate = birthdate

    def age_in_minutes(self):
        today = date.today()
        birth_datetime = datetime.combine(self.birthdate, datetime.min.time())
        today_datetime = datetime.combine(today, datetime.min.time())
        age = today_datetime - birth_datetime
        age_in_minutes = age.total_seconds() / 60
        return round(age_in_minutes)

    def age_in_words(self):
        p = inflect.engine()
        age_in_minutes = self.age_in_minutes()
        words = p.number_to_words(age_in_minutes, andword="").capitalize()
        return f"{words} minutes"

def main():
    try:
        birthdate = datetime.strptime(input("Date of Birth: "), "%Y-%m-%d").date()
        age = Age(birthdate)
        age_in_words = age.age_in_words()
        print(age_in_words)
    except ValueError:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()
