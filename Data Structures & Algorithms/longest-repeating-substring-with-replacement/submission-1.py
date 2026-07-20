class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_frequency = 0
        longest = 0

        for right in range(len(s)):
            char = s[right]
            count[char] = count.get(char, 0) + 1

            max_frequency = max(max_frequency, count[char])

            window_length = right - left + 1

            if window_length - max_frequency >k:
                count[s[left]] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)
        return longest