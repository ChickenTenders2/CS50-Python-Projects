names = []

while True:
    try:
        name = input('Name: ')
        names.append(name)
    except:
        break

if len(names) > 2:
    final_names = ', '.join(names[:-1]) + ", and " + names[-1]
elif len(names) == 2:
    final_names = names[0] + " and " + names[-1]
elif len(names) == 1:
    final_names = names[0]

print("Adieu, adieu, to", final_names)
