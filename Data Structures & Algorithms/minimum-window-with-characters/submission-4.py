from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)
        window = {}

        have = 0
        required = len(need)

        left = 0
        result = [-1, -1]
        min_length = float("inf")

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == required:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    result = [left, right]

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        left, right = result

        return s[left:right + 1] if min_length != float("inf") else ""