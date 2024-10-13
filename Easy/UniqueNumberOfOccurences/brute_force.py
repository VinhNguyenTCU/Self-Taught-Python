from typing import List

class brute_force:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = {}
        s = set()

        for num in arr:
            counter[num] = counter.get(num, 0) + 1

        for num in counter.values():
            if num not in s:
                s.add(num)
            else:
                return False
            
        return True