class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        t=[]
        lenstrs=len(strs)
        for str in strs:
        	
        	l=len(str)
        	
        	t.append(l)
        t.sort()
        sums=sum(t)
        if t[1]==sums/lenstrs:
        	for str in strs:
        		if strs[0] != str:
        			return t[lenstrs-1]	
        	return -1
        return t[lenstrs-1]

s=Solution()
m=s.findLUSlength(["asd","asd","asd"])
print(m)        