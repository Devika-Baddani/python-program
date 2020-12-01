year = int(input("enter year number: "))
if (year%4==0 or year%400 == 0 and year%100!= 0):
    print(year, "is leap year")
else:
    print(year, "is not a leap year")
