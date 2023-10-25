s="""The apple doesn't fall...\nAll that glitters are not gold...\nA picture is worth a thousand words...\nBeggers can't be choosers...\nA bird in the hand...\nBetter safe than sorry...\nAn apple a day keeps the doctor away...\nBlood is thicker than water..."""
print(s)
n=1
b=0
l=list(s)
for i in range(0,len(l)):
    if(l[i]=="\n"):
        n=n+1
print("total number of lines = ",n)
for i in range(0,len(l)):
    if(l[i]=="B"):
        b=b+1
print("number of sentences that start with letter B : ",b)
