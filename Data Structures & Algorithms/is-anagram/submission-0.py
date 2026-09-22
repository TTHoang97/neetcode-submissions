class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths are not the same they can not be an anagram
        if len(s) != len(t):
            return False

        #Initializes the dictionaries so that we can count the strings.        
        countS, countT = {}, {}

        # For each letter in our set add it to their dictionary
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        #Checks if both dictonaries have equal character counts.
        return countS == countT