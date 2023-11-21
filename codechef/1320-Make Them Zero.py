# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    lst=list(map(int,input().split()))
    max=0
    for k in range(n):
        if(lst[k]%2==0 and lst[k]>max):
            max = lst[k]
    power=max//2
    # print(power) -1
    
    check=list(set(lst)) 
    print(check) #2
    
    ans=0
    while(len(check)!=1 and check[0]!=0):
        cut=2**power #2
        for j in range(n):
            if(lst[j]>=cut):
                lst[j]-=cut
                ans+=1
        power-=1
        check=list(set(lst))
        
    print(ans)
    print()