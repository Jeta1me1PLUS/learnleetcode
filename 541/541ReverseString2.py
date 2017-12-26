class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        pass
        m=""
        for l in range(0,len(s),2*k):
        	m+=self.reverseWord(s[l:l+k])
        	m+=s[l+k:l+2*k]
        return m

    def reverseWord(self,str):
    	return str[::-1]
s=Solution()
print(s.reverseStr("abcdefg",2))