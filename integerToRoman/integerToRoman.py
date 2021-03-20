class Solution:
    def intToRoman(self, num: int) -> str:
        values = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D",
                  900: "CM", 1000: "M"}
        roman = ""
        rem = num
        for key in sorted(values, reverse=True):
            while key <= rem:
                roman += values[key]
                rem = rem - key
        return roman

sol = Solution()
t1 = sol.intToRoman(4)
t2 = sol.intToRoman(1994)
t3 = sol.intToRoman(58)

print(t1)
print(t2)
print(t3)


