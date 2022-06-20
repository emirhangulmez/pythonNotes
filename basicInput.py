import datetime
from datetime import date

# Python Refreshing
# Author: Emirhan Gulmez

try:
    # Basic Input Program
    birthYear = input("Enter Birth Date (%d-%m-%Y): ")
    myDate = birthYear
    formattedDate = datetime.datetime.strptime(myDate, "%d-%m-%Y")
    today = date.today()
    year = int(today.strftime("%Y"))
    day = int(today.strftime("%d"))
    month = int(today.strftime("%m"))

    age = 0
    tempAge = year - int(formattedDate.year)
    if int(formattedDate.month) < month:
        age = tempAge
    if int(formattedDate.month) > month:
        age = tempAge - 1
    if int(formattedDate.month) == month:
        age = tempAge
        if int(formattedDate.day) > day:
            age = tempAge - 1

    print(f"Your Age: {age}")
except:
    print("An exception occurred")
