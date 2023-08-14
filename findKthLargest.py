def findKthLargest(nums, k):
    n = len(nums)
    
    while k >= 0:
        big = -10**5
        for i in range(n):
            if nums[i] > big:
                big = nums[i]
        nums.remove(big)
        k -= 1
        n -= 1
    return big

           

nums = [3,2,1,5,6,4]
k = 2
x = findKthLargest(nums, k)
print(x)


        