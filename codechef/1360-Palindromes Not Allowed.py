# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    pick="abcdefghijklmnopqrstuvwxyz";
    if(n<=25):
        print(pick[0:n])
    else:
        ans=""
        entire = ""
        x=n//26
        y=n%26
        entire += pick*x
        rem = pick[0:y]
        ans = entire+rem
        print(ans)