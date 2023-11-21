# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    x=input()
    y=list(x)
    c1 = y.count('1')
    # print(c1)
    ans = (((c1)*(c1+1))//2)
    print(ans)