class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        T=True
        if len(word)==1:
        	return T
        #after 2letter
        for letter in word[1:]:
        	if word[0]>='A' and word[0]<'Z':
        		#print(letter)
        		if word[1]>='A' and word[1]<'Z':
        			if letter>='A' and letter<='Z':
        				T=True
        			else:
        				T=False
        				return T
        		else:
        			if letter>='a' and letter<='z':
        				T=True
        			else:
        				T=False
        				return T
        	else:
        		if letter>='a' and letter<='z':
        			T=True
        		else:
        			T=False
        			return T
        return T
s=Solution()
t=s.detectCapitalUse("GGGd")
print(t)