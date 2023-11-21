# t = int(input())
# for i in range(t):
inp = int(input())
a = 0
b = inp
x = 0
# bool = False
    
a = bin(a)
b = bin(b)
m1 = int(a[2:]) #110
m2 = int(b[2:]) #001010
print(m1)
print(m2)
    
op1 = int(m1&m2)
op2 = int(m1|m2) 

op3 = op1+op2
    
while(a<=x):
    if(op3 == x):
        # bool = True
        print(a,b)
        break
    else:
        a += 1
        b -= 1
        a = bin(a)
        b = bin(b)
        m1 = int(a[2:]) #110
        m2 = int(b[2:]) #001010
        op1 = int(m1&m2)
        op2 = int(m1|m2) 
    
        op3 = op1+op2 
            
    
    
    # while(bool):
    #     m0 = bin(a)
    #     n0 = bin(b)
    #     m0 = int(m0.replace("0b",""))
    #     n0 = int(n0.replace("0b",""))
    #     op1 = m0&n0
    #     print(op1)
    #     op2 = m0|n0
    #     print(op2)
    #     bool = False