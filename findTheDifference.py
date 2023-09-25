
def findTheDifference(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    s1 = list(s)
    s1.sort()
    
    t1 = list(t)
    t1.sort()
    
    for i in range(len(s1)):
            if s1[i] != t1[i]:
                return t1[i]
        
    return t1[len(t1) - 1]

s = "abcd"
t = "abcde"
print(findTheDifference(s, t))