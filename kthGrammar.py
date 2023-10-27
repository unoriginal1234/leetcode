def kthGrammar(n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 1:
            return 0
        
        beg = ['0']
        
        while n > 1:
            nex = []
            for i in beg:
                if i == 0:
                    nex.append('01')
                else:
                    nex.append('10')
            beg = nex
            n -= 1

        x = beg[k - 1]
        ans = int(x)

        return ans

n = 1
k = 1
print(kthGrammar(n , k))