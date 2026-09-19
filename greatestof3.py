n=int(input("enter num1-"))
m=int(input("enter num2-"))
l=int(input("enter num3-"))
if n>m:
    print(n,"is largest than ",m)
elif m>l:
    print(m, "is largest than ",l)
elif n>l:
    print(n," is largest than ",l)
elif m>l:
    print(m," is largst than ",l)
else:
    print(m,"is greater than",l)