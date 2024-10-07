import collections
from typing import Counter, List


class Group_Anagrams:
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        
        ans = collections.defaultdict(list)
        
        for s in strs:
            ans[tuple[sorted(s)]].append(s)

        return ans.values()



    def isValidAnagram(s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

        