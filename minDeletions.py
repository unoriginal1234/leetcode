def minDeletions(s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}
        n = len(s)
        for i in range(n):
            if s[i] in freq:
                freq[s[i]] += 1
            else:
                freq[s[i]] = 1
        
        dict_valuesList = [freq[dict_key] for dict_key in freq]
        dict_valuesList.sort(reverse=True)
        
        m = len(dict_valuesList)
        ans = 0
        for i in range(m - 1):
            if dict_valuesList[i] == dict_valuesList[i + 1]:
                dict_valuesList[i + 1] -= 1
                ans += 1

        return ans


                

s = "aab"
x = minDeletions(s)
print(x)