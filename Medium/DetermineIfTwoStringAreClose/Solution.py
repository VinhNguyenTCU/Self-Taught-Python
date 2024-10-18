from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2): return False

        set1 = set(word1)
        set2 = set(word2)
        map1 = Counter(word1)
        map2 = Counter(word2)

        return set1 == set2 and sorted(map1.values()) == sorted(map2.values())
    
## Time Complexity: O(N).
## The overall time complexity is dominated by the creation of the sets and counters, which is O(n).
## Sorting the values is constant O(1) due to the limited number of characters (26).
## Space Complexity: O(1) since they are bounded by the constant size of the alphabet.