from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        
        n = len(chars)
        if n == 0: return 0
        if n == 1: return 1

        i = 0
        j = 0

        while i < n:
            char = chars[i]
            length = 1
            while (i + length < n) and (chars[i + length] == char):
                length += 1
            chars[j] = char
            j += 1
            if length > 1:
                s = str(length)
                chars[j : j + len(s)] = list(s)
                j += len(s)
            i += length
        return j
            