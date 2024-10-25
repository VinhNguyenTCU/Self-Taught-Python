from typing import Optional
from TreeNode import TreeNode

class RecursiveDFS:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        leftMax = 1 + self.maxDepth(root.left)
        rightMax = 1 + self.maxDepth(root.right)

        return max(leftMax, rightMax)
    
# Time Complexity: O(N)
# Space Complexity: O(1)