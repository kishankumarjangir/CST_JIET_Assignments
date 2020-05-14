a=int(input("Enter number : "))
b=int(input("Enter number : "))
c=int(input("Enter number : "))
n=0
for i in range(1,a+1):
    if(i%b==0 and i%c==0):
        n+=1
print("Special Integer is : ",n)