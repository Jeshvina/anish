n=int(input())
b=[]
c=0
for i in range(n):
    x=int(input())
    b.append(x)
k=int(input())
for i in range(k):
    c+=b[i]
print(c)
