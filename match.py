day = input("Enter a day of the week: ").strip().capitalize()

match day:
    case "Monday":
        print("Gym")
    case "Tuesday":
        print("Read a book")
    case "Wednesday":
        print("Go for a walk")
    case "Thursday":
        print("Study Python")
    case "Friday":
        print("Movie night")
    case "Saturday":
        print("Play football")
    case "Sunday":
        print("Rest and relax")
    case _:
        print("Invalid day entered.")