import calendar

while True:
    print("\n========================================")
    print("          CALENDAR GENERATOR")
    print("========================================")
    print("1. Show Complete Year")
    print("2. Show Specific Month")
    print("3. Check Leap Year")
    print("4. Exit")
    print("========================================")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            year = int(input("Enter year: "))

            print("\n========================================")
            print(f"           CALENDAR {year}")
            print("========================================")
            print(calendar.calendar(year))

        elif choice == "2":
            year = int(input("Enter year: "))
            month = int(input("Enter month (1-12): "))

            if month < 1 or month > 12:
                print(" Please enter a month between 1 and 12.")
            else:
                print("\n========================================")
                print(f"          {calendar.month_name[month]} {year}")
                print("========================================")
                print(calendar.month(year, month))

        elif choice == "3":
            year = int(input("Enter year: "))

            if calendar.isleap(year):
                print(f"{year} is a Leap Year.")
            else:
                print(f" {year} is not a Leap Year.")

        elif choice == "4":
            print("\nThank you for using Calendar Generator!")
            print("Goodbye ")
            break

        else:
            print("Invalid choice. Please select 1-4.")

    except ValueError:
        print(" Please enter a valid number.")