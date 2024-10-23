from typing import List, Optional
from Easy.TreeNode import TreeNode

class BinaryTreePreorderTravesal:
    def preorderTraversal(self, root:Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        stack, ans = [root], []

        while stack:
            root = stack.pop()
            if root is not None:
                ans.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)
        
        return ans
    
    """
    Space Complexity: O(n)    
    Time Complexity: O(n) where n is the number of input nodes
    """
