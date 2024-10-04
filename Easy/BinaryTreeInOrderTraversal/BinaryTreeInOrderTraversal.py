from Easy.TreeNode import TreeNode
from typing import List, Optional

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:  
        res = []
        self.helper(root, res)
        return res
    
    def helper(self, root, res):
        if root is not None:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)

"""
    Time Complexity: O(N) where N is the number of input nodes
    Space Complexity: O(N)
"""

        