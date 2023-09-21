def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int

    Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

    There is only one repeated number in nums, return this repeated number.

    You must solve the problem without modifying the array nums and uses only constant extra space.
    """
    n = len(nums)
    for i in range(n):
        if nums[i] in nums[i +1 : ]:
            return nums[i]

nums = [2,1,2]
x = findDuplicate(nums)
print(x)