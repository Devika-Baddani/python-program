n = int(input("enter a number to print the factorial for: "))
f=1
for i in range(1,n+1):
    f = f*i
print(f, "is the factorial of ",n)
