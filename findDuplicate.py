def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int

    Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

    There is only one repeated number in nums, return this repeated number.

    You must solve the problem without modifying the array nums and uses only constant extra space.
    """
    n = len(nums)
    for i in range(0, n - 1):
        j = i +1
        while j > 0:
            if nums[i] == nums[j]:
                return nums[i]
            j += 1
            if j == n:
                break

nums = [2,1,2]
x = findDuplicate(nums)
print(x)