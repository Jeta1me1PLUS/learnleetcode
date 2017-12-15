class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        nums1 = []
        nums2 = []
        for i in range(len(nums)):
            nums1 += nums[i]
            print(nums1)
        if r * c != len(nums1):
            return nums
        else:
            # for i in range(r):
            #     nums2.append(nums1[i*c: i*c + c])
            # return nums2
            nums3=[]
            for i in range(r):
                for j in range(c):
                    #print(j+c*i)
                    nums3.append(nums1[j+c*i])
                # print(nums3)
                nums2.append(nums3)
                nums3=[]
            return nums2
s=Solution()
print(s.matrixReshape([[1,2],[3,4],[5,6]],2,3))