class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        k=0
        m=''
        vowels=['a','e','i','o','u','A','E','I','O','U']
        for letter in s:
        	if letter in vowels:
        		m+=self.returnVowels(s)[k]	
        		k=k+1
        	else:
        		m+=letter
        return m
    def returnVowels(self,s):
    	"""
    	:type s: str
    	:rtype: str
    	"""
    	str=''
    	vowels=['a','e','i','o','u','A','E','I','O','U']
    	for Svowels in s:
    		if Svowels in vowels:
    			str+=Svowels
    	return str[::-1]
s=Solution()
print(s.reverseVowels("asdfaou"))