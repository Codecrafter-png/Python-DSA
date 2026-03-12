number=int(input("enter a number:"))
temp=number
sum=0
while (temp>0):
    temp2=temp%10
    sum=sum+temp2
    temp//=10
if (number%sum==0):
    print("yeah boii")
else:
    print("ooooo")