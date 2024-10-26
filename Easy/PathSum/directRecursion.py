from typing import Optional
from TreeNode import TreeNode

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        
        targetSum -= root.val
        if root.left == None and root.right == None:
            return targetSum == 0
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
    
 # Time Complexity: O(N)
 # Space Complexity: in the worst case, the tree is completely unbalanced, e.g. 
 # each node has only one child node, the recursion call would occur N times (the height of the tree), 
 # therefore the storage to keep the call stack would be O(N). But in the best case (the tree is completely balanced), 
 # the height of the tree would be log(N). Therefore, the space complexity in this case would be O(log(N)).