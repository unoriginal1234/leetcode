class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool

        Given a string s, 
        check if it can be constructed by taking a substring 
        of it and appending multiple copies of the substring together.
        """
        n = len(s)

        sub = ""

        for i in range(n/2):
            sub = sub + s[i]
            m = len(sub)
            k = n/m
            if sub*k == s:
                return True
         
        return False