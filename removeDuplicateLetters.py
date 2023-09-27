

def removeDuplicateLetters(s):
    """
    :type s: str
    :rtype: str
    """

    letters = []
    for i in s:
        x = s.count(i)
        if x > 1:
            letters.append(i)

    s1 =  list(s)
    
    for i in letters:
        letters.remove(i)
        s1.remove(i)

    ans = ""
    for i in s1:
        ans = ans + i
    
    return(ans)


# s = "bcabc"
# if removeDuplicateLetters(s) == "abc":
#     print('true')
# else:
#     print('false')

s = "cbacdcbc"
if removeDuplicateLetters(s) == "acdb":
    print('true')
else:
    print('false')
    print(removeDuplicateLetters(s))

