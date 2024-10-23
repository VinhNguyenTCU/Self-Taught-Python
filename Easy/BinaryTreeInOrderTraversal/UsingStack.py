from typing import List, Optional
from TreeNode import TreeNode

class UsingStack:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        currNode = root

        while stack or currNode:
            
            while currNode != None:
                stack.append(currNode)
                currNode = currNode.left

            currNode = stack.pop()
            res.append(currNode.val)
            currNode = currNode.right


        return res
    
    # Time Complexity: O(N)
    # Space Complexity: O(N)