from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2): return False

        set1 = set(word1)
        set2 = set(word2)
        map1 = Counter(word1)
        map2 = Counter(word2)

        map3 = {}


        return set1 == set2 and sorted(map1.values()) == sorted(map2.values())