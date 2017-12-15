import numpy as np

class Solution(object):
    def matrixReshape(self, nums, r, c):
        try:
            #return np.reshape(nums, (r, c))
            #tolist是變成list
            return np.reshape(nums, (r, c)).tolist()
        except:
            return nums
s=Solution()
print(s.matrixReshape([[1,2],[3,4],[5,6]],2,3))