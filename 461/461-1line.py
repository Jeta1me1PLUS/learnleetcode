class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #x^y按照位或
        return bin(x^y).count('1')
s=Solution()
print(s.hammingDistance(1,2))