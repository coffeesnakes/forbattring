from socket import AF_APPLETALK


AF_APPLETALK


class Solution(object):
    def containsDuplicate(self, nums):
        count = set()
        
        for i in nums:
            if i in count:
                return True
            else:
                count.add(i)
            
        return false
        """
        :type nums: List[int]
        :rtype: bool
        """
        