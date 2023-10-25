x=int(input("Enter the lower range : "))
y=int(input("Enter the upper range : "))
l=[]
for i in range(x,y):
    for x in range(x,y):
        if(x*x)<y:
            l.append(x*x)
print(l)
