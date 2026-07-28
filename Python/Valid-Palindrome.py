class Solution :
    def isPalindrome(self , s : str) -> bool :
        s = s.lower()
        Alnum = ""
        for ch in s :
            if ch.isalnum():
                Alnum += ch 
        left = 0 
        right = len(Alnum) -1 
        while left < right :
            if Alnum[left] != Alnum[right] :
                return False 
            left += 1
            right -= 1 
        return True
