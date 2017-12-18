class Solution(object):
	def findLUSlength(self, strs):
		def issubsequence(s, t):
			t = iter(t)
			#print(all(c in t for c in s))
			return all(c in t for c in s)

		for s in sorted(strs, key=len, reverse=True):
			print(s)
			print(sum(issubsequence(s, t) for t in strs))
			if sum(issubsequence(s, t) for t in strs) == 1:
				return len(s)
		return -1
s=Solution()
m=s.findLUSlength(["aaa","aa","aaa"])
print(m)