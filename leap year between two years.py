#a = int(input("enter begining year: "))
#b = int(input("enter ending year: "))
for i in range(1900,2101):
    if i%4==0 or i%400==0 and i%100!=0:
        print(i)
