# cook your dish here
t = int(input())
for i in range(t):
    a,b = list(map(int,input().split()))
    # x0 = a+d
    # y0 = (d-1)+b
    if((a-b)<=2 or (b-a)<=2):
        print("YES")
    else:
        print("NO")

    
    