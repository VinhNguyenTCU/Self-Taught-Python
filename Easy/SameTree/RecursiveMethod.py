from typing import Optional, List
from TreeNode import TreeNode

class RecursiveMethod:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        list1 = []
        list2 = []

        self.helper(p, list1)
        self.helper(q, list2)

        return list1 == list2

    
    def helper(self, root: Optional[TreeNode], list:List):
        if root == None:
            list.append(None)
            return
        
        currNode = root
        list.append(currNode.val)

        self.helper(currNode.left, list)
        self.helper(currNode.right, list)

# Time Complexity: O(N)
# Space Complexity: O(N)