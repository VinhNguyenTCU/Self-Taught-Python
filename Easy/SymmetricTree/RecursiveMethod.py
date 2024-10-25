from typing import Optional
from TreeNode import TreeNode

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, root)

    def helper(self, root1: Optional[TreeNode], root2:Optional[TreeNode]) -> bool:
        # If both If both nodes are None, 
        # it means we've reached the end of the branch, 
        # and they are symmetric (mirror images) at this level. 
        # So, it returns True.
        if root1 == None and root2 == None:
            return True

        # If only one of the nodes is None (one subtree is deeper than the other), 
        # they are not symmetric, so it returns False.
        if root1 == None or root2 == None:
            return False
        
        # If the values of the two nodes are different, 
        # they are not symmetric, so it returns False.
        if root1.val != root2.val: 
            return False
        
        return self.helper(root1.left, root2.right) and self.helper(root1.right, root2.left)
    
    # Time Complexity: O(N) Because we traverse the entire input tree once, the total run time is O(n), where n is the total number of nodes in the tree.
    # Space Complexity: O(h) where h is the height of the tree, worst case O(N) where the tree is linear, best case is O(logN) when binary tree is perfectly symmetric and balanced.

    #   1
    #  / \                  
    # 2   2 --> Linear but still result in True     
    # \    \
    #   3   3 

