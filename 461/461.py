class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #return bin(x)[2:],bin(y)[2:]
        xBin,yBin,lenX=self.formattingXY(x,y)
        distance=0
        for t in range(lenX):
            if xBin[t] != yBin[t]:
                distance=distance+1
        
            
        return distance
    def formattingXY(self,x,y):
        xBin=bin(x)[2:]
        yBin=bin(y)[2:]
        x1=len(xBin)
        y1=len(yBin)
        t=x1-y1
        if t<0 :
            xBin=xBin.zfill(y1)
        elif t>0:
            yBin=yBin.zfill(x1)
        return xBin,yBin,len(xBin)
            
s=Solution()

print(s.hammingDistance(1,7))
print(s.formattingXY(1,7))