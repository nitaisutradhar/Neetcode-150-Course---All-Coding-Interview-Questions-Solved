class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement],i]
            numMap[nums[i]] = i
        return []


nums1 = [2,7,11,15]
target1 = 9
solution1 = Solution().twoSum(nums1, target1)
print(f"Input: nums = {nums1}")
print(f"Ouput: {solution1}")