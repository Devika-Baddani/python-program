l_l = int(input("enter lower limit: "))
u_l=int(input("enter upper limit: "))
for n in range(l_l, u_l+1):
    d_n = n
    s = 0
    l = len(str(n))
    while n>0:
        r = n%10
        s = s+r**(l)
        n //= 10
        l = l-1
    if s==d_n:
        print(d_n)
    
