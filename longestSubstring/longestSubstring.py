class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current = ""
        count = 0
        longest = 0
        for char in s:
            if char in current:
                index = current.index(char)
                current = current[index+1:] + char
                count = len(current)
            else:
                count += 1
                current += char
                if count > longest:
                    longest = count
        return longest


sol = Solution()
print(sol.lengthOfLongestSubstring(s="dvdf"))
print(sol.lengthOfLongestSubstring(s="pwwkew"))
