# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    x = list(map(int,input().split()))
    y = sorted(x)
    # print(y)
    max = 0
    if(n==1):
        print(0)
    else:
        count = 0
        for j in range(n-1):
            if(y[j] == y[j+1]):
                count += 1
                if(count>=max):
                    max = count
            else:
                count = 0
        print(n-max-1)