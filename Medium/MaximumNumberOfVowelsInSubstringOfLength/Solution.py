class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        # A string of vowels is created to store the five vowels character
        vowels = "aeiou"

        # Initialize the current max vowels and the total max vowels to 0
        currVowels = maxVowels = 0

        # Traverse the given string to k, which will produce the left most window
        for i in range(k):
            if s[i] in vowels:
                currVowels += 1
        
        # Assign the number of vowels in the leftmost window to the maxVowels
        maxVowels = currVowels 

        # Traverse the remaining string, and each time we move the current window [i - k, i - 1]
        # If we move the window one character to the right, it will become [i - k + 1, i]
        # If the newly added character is a vowel, we incremented currVowels by 1
        # If the newly removed charater s[i - k] is a vowel, we decremented currVowels by 1
        for i in range(k, len(s)):
            if s[i] in vowels:
                currVowels += 1
            if s[i - k] in vowels:
                currVowels -= 1
            
            if currVowels > maxVowels:
                maxVowels = currVowels

        return maxVowels
    
    # Time Complexity: O(N)
    # Space Complexity: O(1)