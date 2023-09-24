import datetime

name = input("Enter your name : ")
print(" what is your birthday date ? ")

year = int(input("Enter year : "))
mon = int(input("Enter month : "))
day = int(input("Enter day : "))

time1 = datetime.date(year,mon,day)
time2 = datetime.date.today()

if mon > time2.month :
    print(name, 'your age is: ', (time2.year - year)-1)
else:
    print(name, 'your age is: ', time2.year - year)

