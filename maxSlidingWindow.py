def maxSlidingWindow(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        You are given an array of integers nums, 
        there is a sliding window of size k which is moving 
        from the very left of the array to the very right. 
        You can only see the k numbers in the window. 
        time the sliding window moves right by one position.

        Return the max sliding window.

        """
        n = len(nums)
        amt = n-k
        if n - k == 0:
            x = [max(nums)]
            return x
        ans = []

        for i in range(amt+1):
            x = -10**5
            for j in range(k):
                if nums[i+j] > x:
                    x = nums[i+j]
            ans.append(x)
        
        return ans

nums = [9,11]
k = 2
y = maxSlidingWindow(nums, k)
print(y)