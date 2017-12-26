class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.count("A")> 1:
        	return False
        else:
        	if "LLL" in s:
        		return False
        	else:
        		return True

s=Solution()
print(s.checkRecord("LPPLPA"))