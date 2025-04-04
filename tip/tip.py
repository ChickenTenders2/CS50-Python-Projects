def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    cost = d.replace("$", "")
    new_cost = float(cost)
    return new_cost

def percent_to_float(p):
    t = p.replace("%", "")
    tip = float(t)
    new_tip = tip/100
    return new_tip

main()
