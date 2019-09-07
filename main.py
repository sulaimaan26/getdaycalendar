import calendarlogic

if __name__ == "__main__":
    get = calendarlogic.GetCal
    print("Enter the date without any zeros for date and month in single digit")
    date = int(input("Enter the day: "))
    month = int(input("Enter the month: "))
    year = int(input("Enter the year: "))
    print("The Corresponding Day for {}/{}/{} is {}".format(date, month, year, get.getday(date, month, year)))
else:
    print("Please run as main file")