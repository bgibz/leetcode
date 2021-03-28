class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        int_as_str = str(x)
        length = len(int_as_str)
        if length < 2:
            return True
        half = int(length / 2)
        front = int_as_str[:half]
        back = int_as_str[-half:][::-1]
        if int(front) == int(back):
            return True
        else:
            return False


sol = Solution()
print(sol.isPalindrome(2222))
print(sol.isPalindrome(234))
print(sol.isPalindrome(343))
print(sol.isPalindrome(-222))
print(sol.isPalindrome(1))
