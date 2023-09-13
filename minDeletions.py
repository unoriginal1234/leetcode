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
            j = i + 1
            while dict_valuesList[i]> 0 and dict_valuesList[i] == dict_valuesList[j]:
                # Can I do a seperate loop here to clear out the long string of similars?
                dict_valuesList[j] -= 1
                ans += 1
                if j == m - 1:
                    break
                else:
                    j += 1

        return ans


                

s = "bbcebab"
x = minDeletions(s)
print(x)