from typing import List

class countDuplicate:
    def count(arr: List[int]) -> int:

        hash_map = {}
        count = 0

        for i in range (len(arr)):
            if arr[i] not in hash_map:
                hash_map[arr[i]] = 1
            hash_map[arr[i]] += 1

        for value in hash_map.values():
            if value > 1:
                count += 1
        
        return count


    print(count([1,3,3,4,4,]))