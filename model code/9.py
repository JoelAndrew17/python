x=int(input("Enter lower range : "))
y=int(input("Enter upper range : "))
l=[]
for i in range(x,y):
    square=0
    square=i*i
    t=(i,square)
    l.append(t)
print(l)
