class Solution(object):
    def isPalindrome(self, x):
        x =  str(x)
        if x == x[::-1]:
            return True
        else: return False
        """
        :type x: int
        :rtype: bool
        """
