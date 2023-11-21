# cook your dish here
t = int(input())
for i in range(t):
    x = input()
    y = list(x)

    if(y.count('0')==1 or y.count('1')==1):
        print("Yes")
    else:
        print("No")