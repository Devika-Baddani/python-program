n = int(input("enter a number: "))
l = len(str(n))
s =0
while n>0:
    r = n%10
    s = s+ r*(10**(l-1))
    n //= 10
    l = l-1
print(s)
    
    
    
