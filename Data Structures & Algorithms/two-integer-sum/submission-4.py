class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #We are looking for two values inside nums that add up to target. There is always a solution.
        #Simple approach is to iterate through the array twice and check if the values match the target return their indices. Time Complexity: O(n**2) Space Complexity: O(1)
        #Better approach is two pointers on a sorted array.

        sortedArray = []
        #Store the sorted Array inside a differnt variable so that we can also store their original positions in the array.
        for i, num in enumerate(nums):
            sortedArray.append([num, i])

        sortedArray.sort()
        i = 0
        j = len(nums) - 1
        #Two pointers i(beginning of array) & j(end of array)
        while i < j:
            #Go through the array increasing i when our sum is less than our target and vice versa with j
            sum = sortedArray[i][0] + sortedArray[j][0]
            if sum < target:
                i += 1
            elif sum > target:
                j -= 1
            elif sum == target:
                #Use min and max so that the return result is always using the number that came first in the array as the first value(in the case of negative integer values of the array.)
                return [min(sortedArray[i][1],sortedArray[j][1]), max(sortedArray[i][1],sortedArray[j][1])]

