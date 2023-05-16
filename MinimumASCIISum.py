def minimumSum(s):
    rs = s[::-1]
    half = len(s) // 2
    palindrome = True
    result = ''
    for i in range(half):
        if s[i] == rs[i] or s[i] == '?' or rs[i] == '?':
            if s[i] == '?':
                result += rs[i]
            else:
                result += s[i]
            pass
        else:
            palindrome = False
            break
    if palindrome:
        if result.count('?') == len(result):
            return 0
        else:
            new_result = result.replace('?','')
            length = len(new_result)
            ans = 0
            for i in range(length-1):
                ans += (((ord(new_result[i]) - ord(new_result[i+1]))**2))**0.5
            return int(ans*2)
    else:
        return -1

print(minimumSum('a????a'))