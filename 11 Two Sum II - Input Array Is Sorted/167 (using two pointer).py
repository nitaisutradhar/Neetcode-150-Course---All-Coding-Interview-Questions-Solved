from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l<r:
            s = numbers[l] +  numbers[r]
            # If the value of the sum is less than the target, then the value of l will be increase by 1.
            # Else value of r will be decreased by 1
            if(s<target):
                l +=1
            elif s == target:
                return [l+1, r+1]
            else:
                r -=1

solution1 = Solution().twoSum([2,7,11,15],9)
print(f"Output: {solution1}")

# Time Complexity: O(n)
# Space Complexity: O(1)