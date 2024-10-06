class greatest_common_divisor:
    def gcdOfStrings(self, str1:str, str2:str) -> str:
        len1, len2 = len(str1), len(str2) 
        """For example: str1 = "ABCABCABC" str2= "ABCABC" 
        then len1 = 9, len2 = 6 """

        def valid(k):
            if len1 % k or len2 % k: 
                return False
            """
            The first check inside valid(k) is whether both len1 and len2 are divisible by k. 
            If either length is not divisbile by k, the substring cannot evenly divide that string,
            so we return False

            For example: if k = 3 and str1 = "ABCABCABC", len1 % k = 0 since 9 is divisible by 3.
            Similary, len2 % k = 0 since 6 is divisble by 3. Therefore, the check passes and we proceed
            """

            n1, n2 = len1 // k, len2 // k
            base = str1[:k]

            """
                For example, with k = 3
                n1 = len1 // k = 9 // 3 = 3 (so str1 should be 3 repetitions of base)
                n2  = len2 // k = 6 // 3 = 2 (so str2 should be 2 repetition of base)

                Then we get the base by cutting str1 --> base = "ABC"
            """

            return str1 == n1 * base and str2 == n2 * base
        
        for i in range(min(len1, len2), 0, -1):
            if valid(i):
                return str1[:i]
            
        return ""


        


