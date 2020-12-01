n = int(input("enter a number: "))
d_n = n
s = 0
while n>0:
    r = n%10
    s = s+r
    n //= 10
if d_n%s == 0:
    print(d_n, "harshad number")
else:
    print(d_n, "is not a harshad number")
