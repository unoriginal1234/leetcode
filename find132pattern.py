def find132pattern(nums):
        """
        :type nums: List[int]
        :rtype: bool
        i < j < k
        nums[i] < nums[k] < nums[j]
        """
        n = len(nums)
        if n < 3:
            return False

        for i in range(n):
            j = i + 1
            while j < n - 1:
                if nums[j] < nums[i]: 
                    j += 1
                    if j >= n - 1:
                        break
                k = j + 1               
                while k < n:
                    if nums[i] < nums[k] and nums[k] < nums[j]:
                        return True
                    else:
                        k += 1  
                    if k > n - 1:
                        break

        
        return False

nums = [3,5,0,3,4]
print(find132pattern(nums))