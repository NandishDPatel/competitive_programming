# n -total people, d - per day capacity, <=9 and >=80 - at risk
import math
t = int(input())
for i in range(t):
    n,d = list(map(int,input().split()))
    arrN = list(map(int,input().split()))
    
    days = 0
    atRisk = 0
    notRisk = 0
    
    for j in range(n):
        if(arrN[j]<=9 or arrN[j]>=80):
            atRisk += 1
        else:
            notRisk += 1

    # print(atRisk)
    # print(notRisk)
    
    if(atRisk == 0):
        print(math.ceil(notRisk/d))
    elif(notRisk == 0):
        print(math.ceil(atRisk/d))
    else:
        x1 = math.ceil(notRisk/d)
        # print(x1)
        x2 = math.ceil(atRisk/d)
        # print(x2)
        print(x1+x2)
            