def generate(numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        
        if numRows == 1:
            return [[1]]
        
        ans = [[1],[1,1]]
        if numRows == 2:
            return [[1],[1,1]]
        
        cur = [1,1]
        
        for i in range(numRows - 2):
            new = cur[:]
            new.append(1)
            for i in range(1, len(new) - 1):
                new[i] = cur[i - 1] + cur[i]
            ans.append(new[:])
            cur = new[:]
        
        
        return ans

x = 5
print(generate(x))