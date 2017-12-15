class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        t=[]
        for numbers in range(left,right+1):
        	if self.isSelfDivNum(numbers)==1:
        		t.append(numbers)
        return t
    def isSelfDivNum(self,number):
        numberStr=str(number)
        if '0' in numberStr:
        	return -1
        for divnum in numberStr:
        	#print(divnum)
        	if number % int(divnum) != 0:
        		return 0
        return 1
s=Solution()
print(s.selfDividingNumbers(1,22))