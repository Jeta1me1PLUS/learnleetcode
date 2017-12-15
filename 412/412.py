class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        List=[]
        for x in range(n+1):
            if x==0:
                continue
            elif self.fizz(x):
                if self.buzz(x):
                    List.append("FizzBuzz")
                else:
                    List.append("Fizz")
            elif self.buzz(x):
                List.append("Buzz")
            else:
                List.append(str(x))
        
        return List
    def fizz(self,n):
        """
        :type n: int
        :rtype: boolean
        """
        if n % 3==0:
            return True
        else:
            return False
    def buzz(self,n):
        """
        :type n: int
        :rtype: boolean
        """
        if n % 5==0:
            return True
        else:
            return False
s=Solution()
print(s.fizzBuzz(15))