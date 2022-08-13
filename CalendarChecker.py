print("Welcome to Sir_Roll's Calendar Checker")

try:
    def roll():
        import calendar
        year = int(input("Enter the year ["))
        month = int(input("Enter the month ["))
        x=calendar.month(year,month)
        print(x)
        print("Would you like to check another one?")
        print("command list:__"
              " 'yes', ",
              " 'no' ")
        response = input("Enter command:__[")
        if response.lower == 'yes':
            roll()
        elif response == 'no':
            print("Thanks for your time, hoping to see you again")
        else:
            print("Command error ^_^ ")
            print("Please start again")
            return roll()

    roll()

except ValueError:
    print("Input Invalid.")
    roll()
