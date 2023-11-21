n = int(input())
m,c = list(map(int,input().split()))

sum1 = 0
sum2 = 0
for i in range(n):
    x1,y1,p1 = list(map(int,input().split()))
    
    y = m*x1 + c
    # print(y)
    if(y1<y):
        sum1 += p1
    else:
        sum2 += p1
        
if(sum1>=sum2):
    print(sum1)
else:
    print(sum2)