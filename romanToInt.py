def romanToInt(s):
    """
    :type s: str
    :rtype: int
    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
    
    """

    num = {
        'O' : 0,
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000,
        }
    
    
    s = s + 'O'
    x = 0
    for i in range(len(s)):
        if s[i]=='I' and s[i + 1]=='V' or s[i]=='I' and s[i + 1]=='X' or s[i]=='X' and s[i + 1]=='L' or s[i]=='X' and s[i + 1]=='C' or s[i]=='C' and s[i + 1]=='D' or s[i]=='C' and s[i + 1]=='M':
            x = x - num[s[i]]
        else:
            x = num[s[i]] + x
    
    return x

s = "MCMXCIV"
ans = romanToInt(s)
print(ans)