class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        letter='abcdefghigklmnopqrstuvwxyz'
        index=[s.index(l) for l in letter if s.count(l)==1]
        return min(index) if len(index)>0 else -1 
s=Solution()
print(s.firstUniqChar("asdfas"))
