num = int(input("enter a number: "))
d_num = num
s = 0
while num>0:
    r = num%10
    s = s + r**3
    num //= 10
if s== d_num:
    print(d_num, "is an amstrong number")
else:
    print(d_num, "is not an amstrong number")
    
