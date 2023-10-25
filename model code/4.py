S1=str(input("Enter frist string : "))
S2=str(input("Enter Second String : "))
a=len(S1)
b=len(S2)
count=0
if(a>b):
    c=b
else:
    c=a
for i in range(0,c):
    if(S2[i]==S1[i]):
        count=count+1
print(count)
