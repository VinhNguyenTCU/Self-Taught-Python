class UsingFrequencyArray:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2): return False

        map1 = [0] * 26
        map2 = [0] * 26

        for c in list(word1):
            map1[ord(c) - ord('a')] += 1

        for c in list(word2):
            map2[ord(c) - ord('a')] += 1
        
        # Since 26 is constant, the time complexity for this loop is O(1).
        for i in range(26):
            if (map1[i] == 0 and map2[i] > 0) or (map1[i] > 0 and map2[i] == 0):
                return False

        # Sorting the map1 and map2 arrays each takes O(26 log 26) = O(1) since the array size is constant (26).
        return sorted(map1) == sorted(map2)
    
# Time Complexity: O(M + N) where N is the length of word1 and M is the length of word2; however, they have to have the same size
#                  so O(N + N) = O(2N) = O(N)
# Space Complexity: O(1)
