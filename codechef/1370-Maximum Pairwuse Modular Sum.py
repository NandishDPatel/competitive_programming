# cook your dish here
t = int(input())
for i in range(t):
    n,m = list(map(int,input().split()))
    arrA = list(map(int,input().split()))
    max = 0
    arrB = sorted(arrA)
    ai = arrB[-1]
    aj = 0
    total = 0
    diff = 0
    term = 0
    max = 0
    total = ai + aj + term
    for j in arrB[::-1]:
        aj = j
        diff = aj-ai
        term = diff%m
        total = ai+aj+term
        if(total>max):
            max = total
    print(max)