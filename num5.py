l1=int(input())
b=list(map(int,input().split()))
b.sort(reverse=True)
c=0
for i in range(0,int(len(b))):
    c=(c*10)+b[i]
print(c)
