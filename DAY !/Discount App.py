a=float(input("enter item 1 price:"))
b=float(input("enter item 2 price:"))
c=int(input("enter discount prercentage:"))
d=a+b
print(d)
print(round(d-(d*c/100),2))
print(round(d*(c/100),2))
