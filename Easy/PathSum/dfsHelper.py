from typing import Optional
from TreeNode import TreeNode

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(currNode: Optional[TreeNode], currSum: int):
            if currNode == None:
                return False
            
            currSum += currNode.val
            if currNode.left == None and currNode.right == None:
                return currSum == targetSum
            
            return dfs(currNode.left, currSum) or dfs(currNode.right, currSum)
        
        return dfs(root, 0)
    
    # Time Complexity: O(N)
    # Space Complexity: in the worst case, the tree is completely unbalanced, e.g. 
    # each node has only one child node, the recursion call would occur N times (the height of the tree), 
    # therefore the storage to keep the call stack would be O(N). But in the best case (the tree is completely balanced), 
    # the height of the tree would be log(N). Therefore, the space complexity in this case would be O(log(N)).