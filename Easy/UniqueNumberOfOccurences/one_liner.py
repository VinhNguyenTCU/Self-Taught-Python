from typing import List
from collections import Counter

class one_liner:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(set(Counter(arr).values())) == len(set(arr))