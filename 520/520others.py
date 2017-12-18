#使用三個方法
class Solution(object):
    def detectCapitalUse(self, word):
    	return word.isupper() or word.islower() or word.istitle()
s=Solution()
t=s.detectCapitalUse("GGGd")
print(t)
