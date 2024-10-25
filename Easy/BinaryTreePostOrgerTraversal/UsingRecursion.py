from typing import List, Optional
from TreeNode import TreeNode

class UsingRecursion:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        currNode = root
        res = []

        self.helper(currNode, res)
        return res
    
    def helper(self, currNode : TreeNode, res: List) -> None:
        if currNode is None:
            return
        
        if currNode.left != None:
            self.helper(currNode.left, res)
        if currNode.right != None:
            self.helper(currNode.right, res)
        res.append(currNode.val)
    
    


        
