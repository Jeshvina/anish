n=int(input())
flag=0
if(n>2):
    for i in range(2,n):
        if((n%i)==0):
            flag=1
            break
else:
    print("yes")
if(flag==0):
    print("yes")
else:
    print("no")
