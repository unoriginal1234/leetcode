def minimizeMax(nums, p):

    if p <= 0:
        return 0
    # sort numbers
    nums.sort()
    n = len(nums)
    # tack on a little 0 at the end to iterate this
    nums.append(0)
    # Create a list of differences, these will be sorted from 
    # smallest to largest because of the sort
    List = []
    for i in range(n):
        List.append(nums[i+1]-nums[i])
    List.pop(n-1)
    List.sort()
    # I now have a list of the differences from smallest to largest 
    # (I might have to pop of the last one because it's fake)
    ans = []
    while p>0:
        ans.append(List[p-1])
        p -= 1
    # Now this is a list of p differences
    x = max(ans)
    return x

    

    # Find the smallest pairs of numbers in the list for p*2

    """
    :type nums: List[int]
    :type p: int
    :rtype: int
    
    You are given a 0-indexed integer array nums and an integer p. 
    Find p pairs of indices of nums such that the maximum difference 
    amongst all the pairs is minimized. 
    Also, ensure no index appears more than once amongst the p pairs.

    Note that for a pair of elements at the index i and j, 
    the difference of this pair is |nums[i] - nums[j]|, 
    where |x| represents the absolute value of x.

    Return the minimum maximum difference among all p pairs. 
    We define the maximum of an empty set to be zero.

    Constraints:
    1 <= nums.length <= 105
    0 <= nums[i] <= 109
    0 <= p <= (nums.length)/2
    """
nums = [3,4,2,3,2,1,2]
p = 3
x = minimizeMax(nums, p)
print(x)
