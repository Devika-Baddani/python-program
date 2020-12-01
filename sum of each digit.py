num = int(input("enter a number: "))
s = 0
while num>0:
    r = num%10
    s = s+r
    num //= 10
print(s, "is the sum of each digit in the number")
