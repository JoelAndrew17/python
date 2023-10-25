s="""this is the most straightforward way to count the number\nof lines in a text file in python. the readlines() method reads all\nlines from a file and stores it in a list. Next, use the len() function\nto find the length of the list which is nothing but total lines present in a file."""
print(s)
n=0
c=0
j=0
h=0
w=0
e=0
l=list(s)
for i in range(0,len(l)):
    if(l[i]=="\n"):
        n=n+1
print("number of lines = ",n)
for i in range(0,len(l)):
    if(l[i]=="\n"):
        c=c+1
    if c==0:
        if(l[i]==' '):
            j=j+1
    elif c==1:
        if(l[i]==' '):
            h=h+1
    elif c==2:
        if(l[i]==' '):
            w=w+1
    elif c==3:
        if(l[i]==' '):
            e=e+1
print("line1 = ",j+1,"\nline2 = ",h+1,"\nline3 = ",w+1,"\nline4 = ",e+1)
