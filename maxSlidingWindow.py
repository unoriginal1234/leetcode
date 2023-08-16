def maxSlidingWindow(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
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