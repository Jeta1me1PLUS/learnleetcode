class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        sum = 0
        zhuangtai=0
        for x in ops:
            if x=="D":
                zhuangtai=zhuangtai*2
                sum=sum+zhuangtai
                
            elif x=="C":
                sum=sum-zhuangtai
                
            elif x=="+":
                sum=zhuangtai+zhuangtai1+sum
                zhuangtai=zhuangtai+zhuangtai1
            else:
                x=int(x)
                zhuangtai=x
                sum=sum+x
            #
            #如何保存上两个状态
            #
            zhuangtai1=sum-zhuangtai
            print(x,sum)
            
            #print(zhuangtai)
            #print(zhuangtai1)            
            print("\n")
        return sum
s=Solution()
print(s.calPoints(["5","-2","4","C","D","9","+","+"]))