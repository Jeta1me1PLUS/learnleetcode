class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        k=[]
        for t in words:
            if self.findthisWordsinlist(t):
                
                k.append(t)
                    
        return k
        
    def findthisWordsinlist(self, words):
        List1=['q','w','e','r','t','y','u','i','o','p']
        List2=['a','s','d','f','g','h','j','k','l']
        List3=['z','x','c','v','b','n','m']
        if self.findwordinList(words.lower(),List1) or self.findwordinList(words.lower(),List2) or self.findwordinList(words.lower(),List3):
            return True
        else:
            return False
            
    def findwordinList(self,words,List):
        k=0
        for t in words:
            if t in List:
                k=k+1   
        if k == len(words):
            return True
        else:
            return False
s=Solution()
print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))
