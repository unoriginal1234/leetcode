
def sortArrayByParity(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        odds = []
        ans = []
             
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                odds.append(nums[i])
            else:
                ans.append(nums[i])
        

        ans.extend(odds)
        print(ans)

nums = [3,1,2,4]
sortArrayByParity(nums)