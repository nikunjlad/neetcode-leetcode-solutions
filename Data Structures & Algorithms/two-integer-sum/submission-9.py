class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 2:
            return [0,1]

        left = 0
        right = len(nums) - 1

        indexed = sorted(enumerate(nums), key=lambda x: x[1])

        while left < right:
            if indexed[left][1] + indexed[right][1] == target:
                if indexed[left][0] < indexed[right][0]:
                    return [indexed[left][0], indexed[right][0]]
                else:
                    return [indexed[right][0], indexed[left][0]]
            elif indexed[left][1] + indexed[right][1] > target:
                right -= 1
            else:
                left += 1
            