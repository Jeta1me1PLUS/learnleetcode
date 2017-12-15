class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        flat = sum(nums,[])
        print(flat)
        if len(flat) != r * c:
            return nums
        tuples = zip(*([iter(flat)] * c))
        return list(map(list, tuples))
s=Solution()
print(s.matrixReshape([[1,2],[3,4],[5,6]],3,2))