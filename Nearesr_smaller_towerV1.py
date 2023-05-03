result = []
for i in range(len(arr)):
    x = 1
    while True:
        if i-x < 0:
            left = -1
            lgap = x
            break
        if arr[i-x] < arr[i]:
            left = i-x
            lgap = x
            break
        x += 1
    
    x = 1
    while True:
        if i+x > (len(arr)-1):
            right = -1
            rgap = x
            break
        if arr[i+x] < arr[i]:
            right = i+x
            rgap = x
            break
        x += 1
    if lgap <= rgap and left != -1:
        result.append(left)
    else:
        result.append(right)
        print(lgap,left,rgap,right)
print(result)