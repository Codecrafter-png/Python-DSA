number=int(input("Enter the number:"))
temp=number
sum=0
while temp>0:
digit =temp%10
fact=1
for i in range(1,digit+1):
fact=fact*i
sum=sum+fact
temp=temp//10

if (number==sum):
print("yahoooooo")
else:
print("nottu")