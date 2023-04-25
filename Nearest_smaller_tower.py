arr1 = [7,3,4,1,5,10,1,1]
result = []

for i in range(len(arr1)):
    lend = False
    rend = False
    x = -1
    temp = i
    possible_ans = []
    
    while True:
        print(x+temp)
        if x+temp < 0:
            lend = True
            pass
        elif x+temp > len(arr1)-1:
            rend = True
            pass
        elif arr1[i] > arr1[x+temp]:
            possible_ans.append(arr1[x+temp])
            
            if x+temp < i:
                new = x+temp+2
            else:
                new = x+temp-2
            if new < 0:
                pass
            elif new > len(arr1)-1:
                pass
            elif arr1[i] > arr1[new]:
                possible_ans.append(arr1[x+temp])
            result.append(min(possible_ans))
            break
            
    
        if lend == True and rend == True:
            result.append(-1)
            break
        
        temp = x+temp
        if x > 0:
            x+=1
        else:
            x-=1
        x*=-1

print(result)
        