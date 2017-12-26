class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        letters='abcdefghijklmnopqrstuvwxyz'
        # index() 函数用于从列表中找出某个值第一个匹配项的索引位置。
        # 列表生成式
        index=[s.index(l) for l in letters if s.count(l) == 1]
        print(index)
        return min(index) if len(index) > 0 else -1
s=Solution()
print(s.firstUniqChar("asdfas"))
