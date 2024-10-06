from typing import List

""" This method uses two pointer
    Time Complexity: O(m + n)
    Space Complexity: O(m + n), because we do not consider the space consumed by the input string, 
    so the space complexity would be O(1)
"""

class merge_string_alternately:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left, right = 0, 0
        m, n = len(word1), len(word2)
        res = []

        while left < m or right < n:
            if left < m:
                res.append(word1[left])
            if right < n:
                res.append(word2[right])

        return ''.join(res)
    
sol = merge_string_alternately()
result = sol.mergeAlternately("abc", "qpr")
print(result)