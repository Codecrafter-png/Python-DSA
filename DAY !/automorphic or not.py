number=int(input("enter a number:"))
square=number*number
length=len(str(number))
square_digit=square%10**(length)
if(number==square_digit):
    print("automorphic")
else:
    print("not automorphic")