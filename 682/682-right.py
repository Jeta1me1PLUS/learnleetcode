class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        a=[]
        for x in ops:
            if x=='C':
                a.pop()
            elif x=='D':
                a.append(a[-1]*2)
            elif x=='+':
                a.append(a[-1]+a[-2])
            else:
                a.append(int(x))
        a=sum(a)
        return a 
s=Solution()
print(s.calPoints(["5","-2","4","C","D","9","+","+"]))