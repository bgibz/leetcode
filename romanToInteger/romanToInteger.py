class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ret = 0
        last = 0
        for c in s[::-1]:
            curr = values[c]
            if curr < last:
                ret -= curr
            else:
                ret += curr
            last = curr
        return ret

test = "III"
test2 = "IX"
test3 = "LVIII"
sol = Solution()
print(sol.romanToInt(s=test))
print(sol.romanToInt(s=test2))
print(sol.romanToInt(s=test3))
