strings = []
for _ in range(int(input())):
    strings.append(input())


result = ""

for k in strings[0]: #h,o,p,e
    count = 0
    
    for j in strings[1:]: #elephant and path
        
        if k not in j:
            count += 1
    
    if count == 0:
        result += k
        
        for i in range(1,len(strings)): 
            strings[i] = strings[i].replace(k,'',1)
            

if len(result) == 0:
    print('no such string')
print(''.join(sorted(result)))
    