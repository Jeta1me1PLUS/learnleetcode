class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
       	if a==b:
       		return-1
       	else:
       		t=max(len(a),len(b))
       	return t
s=Solution()
t=s.findLUSlength('aaa','aaa')
print(t)

