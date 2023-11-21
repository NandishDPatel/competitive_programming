# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    arrH=list(map(int,input().split()))
    
    counts=[]
    for j in range(n):
        current=1
        if(arrH[j]!=-1):
            for k in range(j+1,n):
                if(arrH[j]==arrH[k]):
                    current+=1
                    arrH[k]=-1
            counts.append(current)
    print(counts)
    if(len(counts)==1):
        print(0)
    elif(len(set(counts))==1):
        print(0)
    