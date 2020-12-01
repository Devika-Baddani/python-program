a = int(input("enter first number: "))
b = int(input("enter second number: "))
if a>b:
    m = b
else:
    m = a
while m>0:
    if a%m==0 and b%m==0:
        g = m
        break
    m = m-1
print(g," is the G.C.D of ",a, "and", b)
