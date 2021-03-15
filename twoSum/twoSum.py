class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        passed = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in passed:
                return [passed[remainder], i]
            else:
                passed[nums[i]] = i


# Tests
test = [2, 7, 11, 15]
solution = Solution()
res = solution.twoSum(nums=test, target=9)
print(res)
## [0, 1]

test2 = [3, 3]
res = solution.twoSum(nums=test2, target=6)
print(res)
# [0, 1]

test3 = [3, 2, 4]
res = solution.twoSum(nums=test3, target=6)
print(res)