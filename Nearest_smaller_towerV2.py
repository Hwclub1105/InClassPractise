arr1 = [4, 8, 6, 5, 3, 8, 5, 5]
result = []

for i in range(len(arr1)):
    lend = False
    rend = False
    x = -1
    temp = i
    possible_ans = {}
    
    while True:
        print(x+temp)
        if x+temp < 0:
            lend = True
            pass
        elif x+temp > len(arr1)-1:
            rend = True
            pass
        elif arr1[i] > arr1[x+temp]:
            print({arr1[i]},' > ',{arr1[x+temp]})
            possible_ans[arr1[x+temp]] = x+temp 
            temp = x+temp
            if x > 0:
                x+=1
            else:
                x-=1
            x*=-1
            if x+temp < 0:
                pass
            elif x+temp > len(arr1)-1:
                pass
            elif arr1[i] > arr1[x+temp] and x+temp > i:
                possible_ans[arr1[x+temp]] = x+temp 
            result.append(possible_ans[min(possible_ans)])
            print(possible_ans)
            print(possible_ans[min(possible_ans)])
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
        