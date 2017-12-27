class Solution(object):
    def reverseVowels(self, s):
        vowels=set(list("aeiouAEIOU"))
        s=list(s)
        prt_1,prt_2=0,len(s)-1
        while  prt_1<prt_2:
            if s[prt_1] in vowels and s[prt_2] in vowels:
                s[prt_1],s[prt_2]=s[prt_2],s[prt_1]
                prt_1+=1
                prt_2-=1
            if s[prt_1] not in vowels:
                prt_1+=1
            if s[prt_2] not in vowels:
                prt_2-=1
        return ''.join(s)
s=Solution()
print(s.reverseVowels("asdfczaoe"))