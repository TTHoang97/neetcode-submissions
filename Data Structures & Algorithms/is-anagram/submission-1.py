class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #s should have the save characters as t
        #we can sort s and t and see if they are equal(kind of brute force)

        #Quick check if they are already equal strings.
        if s == t:
            return True

        return sorted(s) == sorted(t)