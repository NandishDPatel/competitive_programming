t = int(input())
for i in range(t):
    n = int(input())
    y = 10**(n-1)
    x = y #1
    bool = True

    while(bool):
        x+=1
        if(x%3 == 0 and x%9!=0 and x%2 != 0):
            l = x
            check = [int(y) for y in str(l)]
            print(check)
            if 0 in check:
                print("Hi")
            else:
                bool = False
                ans = x
                break
            
        
    
    print(ans)
    