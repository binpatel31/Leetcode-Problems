####################### OPTIMAL ###################
'''
class Solution(object):
    def build(self,helperInorder,preorder,start,end,nextt):
        if start > end:
            return nextt,None
        
        i = helperInorder.index(preorder[nextt])
        nextt+=1
        
        node = TreeNode(helperInorder[i])
        node.left = None
        node.right = None
        if start==end:
            return nextt,node
        
        
        nextt,node.left = self.build(helperInorder,preorder,start,i-1,nextt)
        nextt,node.right = self.build(helperInorder,preorder,i+1,end,nextt)
        return nextt,node
        
        
        
    
    def buildTree(self, preorder, inorder):
        a,b= self.build(inorder,preorder,0,len(inorder)-1,0)
        return b
'''
########################    MY SOLUTION   ####################33
class Solution(object):
    def build(self,valueOfRoot,helperInorder,preorder,nextt):
        node = TreeNode(valueOfRoot)
        leftList = []
        rightList = []
        i = helperInorder.index(valueOfRoot)
        leftList = helperInorder[0:i]
        rightList = helperInorder[i+1:]
        
        leftroot = None
        if len(leftList) > 1:
            leftroot = preorder[nextt]
            nextt+=1
            nextt,node.left = self.build(leftroot,leftList,preorder,nextt)
            
        elif len(leftList) == 0:
            node.left = None
        else:
            lft = TreeNode(leftList[0])
            nextt+=1
            lft.left = None
            lft.right = None
            node.left = lft
        
        rightroot = None
        if len(rightList) > 1:
            rightroot = preorder[nextt]
            nextt+=1
            nextt,node.right = self.build(rightroot,rightList,preorder,nextt)
            
        elif len(rightList) == 0:
            node.right = None
        else:
            rgt = TreeNode(rightList[0])
            nextt+=1
            rgt.left = None
            rgt.right = None
            node.right = rgt
            
        return nextt,node        
        
    
    def buildTree(self, preorder, inorder):
        if len(preorder)==0 or len(inorder)==0:
            return None
        a,b =  self.build(preorder[0],inorder,preorder,1)
        return b
