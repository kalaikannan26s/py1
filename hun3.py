n1=int(input())
n=0
array=input().split(" ")
array.sort(reverse=True)
for a in range(0,n1):
    n*=10
    n+=int(array[a])
print(n)
