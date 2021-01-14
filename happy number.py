n = int(input("enter a number: "))
d_n = n
s = 0
while n>0:
    r = n%10
    s = s+r**2
    n //= 10
    if s==1:
        print(d_n)
        break
    else:
        n = s
