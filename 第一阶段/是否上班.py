
while True:
    day = input("enter a day from monday to sunday， and enter 'q' to quit")
    week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if day == 'q':
        break
    if day not in week:
        print("you must enter a day from monday to sunday")
        continue

    if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
        print("work")
    else:
        print("play")

