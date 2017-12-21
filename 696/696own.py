class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        chunk,consecutive,res=[],1,0
        for i in range(1,len(s)):
        	if s[i]==s[i-1]:
        		consecutive+=1
        	else:
        		chunk.append(consecutive)
        		consecutive=1
        chunk.append(consecutive)
        # return(chunk)
        k=0
        for i in range(0,len(chunk)-1):
        	k+=min(chunk[i],chunk[i+1])
        print(k)
s=Solution()
print(s.countBinarySubstrings("1100011"))