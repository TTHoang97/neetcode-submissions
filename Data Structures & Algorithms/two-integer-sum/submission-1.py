class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #We are looking for two values inside nums that add up to target. There is always a solution.
        #Simple approach is to iterate through the array twice and check if the values match the target return their indices.

        for num1 in range(len(nums)):
            #Start from the next number in the array so that we do not repeat and check the number against itself
            for num2 in range(num1 + 1, len(nums)):
                if nums[num1] + nums[num2] == target:
                    return [num1,num2]