n = int(input("enter n to find the average: "))
s=0
for i in range(n+1):
    s = s+i
    a = s/n
print("the average of first", n," natural numbers is", s/n)
