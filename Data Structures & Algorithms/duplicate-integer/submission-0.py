class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num1 in nums:
            if num1 in seen:
                return True
            seen.add(num1)

        return False