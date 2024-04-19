import csv
from datetime import datetime
import time

now = datetime.now()
date = now.day
day = now.strftime("%A")
month = now.strftime("%B")
year = now.year


def countdown():
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)

def later():
    print('Okay Good Luck')
    return

def is_data_exist_for_today():

    with open('reportmood.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[2] == day and int(row[1]) == month and int(row[3]) == year:
                return True
    return False


def Mood ():
    if is_data_exist_for_today():
        print("You already report mood.")
        countdown()
        return

    data = [
        [date,month,day,year,'Mood']    
        # ['Date','Month','Day','Year','Mood']
    ]

    file = open('reportmood.csv', 'a', newline='')
    write = csv.writer(file)

    write.writerows(data)

    print('Yeayy nice bro. hope tommorow your mood same like today')
    countdown()

def NotMood ():
    if is_data_exist_for_today():
        print("You already report mood.")
        countdown()
        return

    data = [
        [date,month,day,year,'Not Mood']    
        # ['Date','Month','Day','Year','Mood']
    ]

    file = open('reportmood.csv', 'a', newline='')
    write = csv.writer(file)

    write.writerows(data)

    print('Ah Hope you get mood better')
    countdown()

def selection():
    if is_data_exist_for_today():
        print("You already report mood.")
        countdown()
        return

    print('What your mood today:')
    print('1. Mood')
    print('2. Not Mood')
    print('3. Later')
    selection=int(input("Enter your choice: "))
    if selection==1:
        Mood()
    elif selection==2:
        NotMood()
    elif selection==3:
        later()
    else:
        print('Invalid Choice')


selection()