class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        max = 2**31 - 1
        min = -2**31
        flip = False
        if x < 0:
            flip = True
            x = x * -1
        while x != 0:
            pop = int(x % 10)
            x = int(x/10)
            rev = int(rev * 10 + pop)
            if rev > max or (rev == max and pop > 7):
                return 0
            if rev < min or (rev == max and pop < -8):
                return 0
        if flip:
            rev = rev * -1
        return rev


sol = Solution()
print(sol.reverse(221))
print(sol.reverse(-321))
print(sol.reverse(1534236469)) #9646324351