# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def ansTraverse(root, counter):
            if root is None:
                return
                       
            counter[root.val] += 1

            ansTraverse(root.left, counter)
            ansTraverse(root.right, counter)
        
        counter = defaultdict(int)
        ansTraverse(root, counter)
        max_freq = max(counter.values())

        ans = []
        for key in counter:
            if counter[key] == max_freq:
                ans.append(key)
        
        return ans