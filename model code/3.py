n=int(input("enter the number : "))
d,rev=0,0
while(n>0):
    d=n%10
    rev=rev+d
    n=n//10
print(rev)
