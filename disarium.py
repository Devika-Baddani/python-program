n = int(input("enter a number: "))
d_n = n
s = 0
l = len(str(n))
while n>0:
    r = n%10
    s = s+r**(l)
    n //= 10
    l = l-1
if s==d_n:
    print(d_n," is a disarium number")
else:
    print(d_n," is not a disarium number")
