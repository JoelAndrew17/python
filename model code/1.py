p=int(input("Enter the number : "))
result=0
for i in range(1,p):
    if(p%i==0):
        result=result+i
if(p==result):
    print("Perfect number")
else:
    print("not perfect")
