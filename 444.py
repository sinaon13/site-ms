def func(n,count,su,m,cou):
    
    if su==len(n):
        count.append(cou)
    if m==0:
        return 
         
    for i in range(m):
        for j in range(1,n[i]):
            func(n,count,su+j,m-1,cou+1)


m=int(input())
b=(input())
h=b.split()
n=[]
for i in range(m):
    n.append(int(h[i]))
count=[]
cou=0
su=0

##    print(n)
##    print(count)
##    print(su)
##    print(m)
##    print(cou)
func(n,count,su,m,cou)
print((count))
