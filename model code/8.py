s=int(input("enter size : "))
l=[]
for i in range(0,s):
    x=int(input())
    l.append(x)
for i in range(0,s-1):
    for j in range(0,s-1):
        if l[j]<l[j+1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
print(l)
A=int(input("enter the Nth largest element u want to find : "))
print(l[A-1])
