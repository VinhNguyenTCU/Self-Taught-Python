class subsequence:
    def issubsequence(s:str, t:str) -> bool:
        left = 0
        right = 0
        m = len(s)
        n = len(t)

        while right < n and left < m:
            if s[left] == t[right]:
                left += 1
            right += 1
        
        return left == len(s)

