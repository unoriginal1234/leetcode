def decodeAtIndex(s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # print(ord("2"))
        # print(ord("9"))
        # print(ord("a"))
        # print(ord("z"))

        ans = ""
        for i in s:
            if ord(i) < 58:
                ans = ans * (int(i))
            else: 
                ans = ans + i
            if len(ans) >= k:
                return(ans[k - 1])
        

s = "leet2code3"
k = 10
print(decodeAtIndex(s, k))