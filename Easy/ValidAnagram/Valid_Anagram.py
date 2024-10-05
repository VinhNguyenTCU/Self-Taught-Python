class Valid_Anagram:
    def isAnagram(s: str, t: str) -> bool:
        if len(s) != len(t): return False

        map = {}

        for i in range(len(s)):
            if s[i] in map:
                map[s[i]] += 1
            else:
                map[s[i]] = 1

            if t[i] in map:
                map[t[i]] -= 1
        
        for i in range(len(map)):
            if (map[s[i]] != 0): return False

        return True

        