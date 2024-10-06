class use_stack:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeuioAEUIO"
        vowels_stack = []
        ans = []

        for i in range(len(s)):
            if s[i] in vowels:
                vowels_stack.append(s[i])

        for i in range(len(s)):
            if s[i] in vowels:
                ans.append(vowels_stack.pop)
            else:
                ans.append(s[i])

        return ''.join(ans)