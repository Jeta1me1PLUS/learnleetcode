class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        numt=self.toBin(num)
        numt=len(numt)
        str=numt*'1'
        num=num^int(str,2)
        return num
    def toBin(self,num):
        return bin(num)[2:]
