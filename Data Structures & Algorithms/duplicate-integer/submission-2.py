class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for firstNum in range(len(nums)):
            for secondNum in range(firstNum+1, len(nums)):
                if nums[firstNum] == nums[secondNum]:
                    return True

        return False