############3 GOOD ONE ###################################3
'''
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
            
        stack = [(root, float('-inf'), float('inf')), ] 
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True
'''

#####################3 MY SOLUTION #####################3

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def finditout(self,root,ans):
        if root == None:
            return ans
        ans = self.finditout(root.left,ans)
        ans.append(root.val)
        ans = self.finditout(root.right,ans)
        return ans
        
    def isValidBST(self, root):
        ans =  self.finditout(root,[])
        for i in range(len(ans)-1):
            if ans[i] >= ans[i+1]:
                return False
        return True
