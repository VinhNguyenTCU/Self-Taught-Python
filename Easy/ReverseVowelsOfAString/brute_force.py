class brute_force:
    def reverseVowels(s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        ans, rev = [], []
        index, pointer = 0, 0

        for i in range(len(s)):
            if s[i] in vowels:
                rev.append(s[i])
                index += 1
        
        rev.reverse()
        print(vowels)

        for i in range(len(s)):
            if s[i] in vowels:
                ans.append(rev[pointer])
                pointer += 1
            else: ans.append(s[i])

        return ''.join(ans)