# cook your dish here
t=int(input())
for i in range(t):
    x=input()
    y=list(x)
    # print(y)
    cpt = x.title()

    if " " in y:
        lst=list(cpt)
        # print(lst)
        word=""
        lastWrd=""
        ans1=""
        for j in lst:
            # print(j)
            
            if(j==" "):
                ans1 = ans1 + word[0] + ". "
                lastWrd=""
                word=""
            else:
                word+=j
                lastWrd+=j
        ans1 = ans1 + lastWrd
        print(ans1)
            
    else:
        print(cpt)