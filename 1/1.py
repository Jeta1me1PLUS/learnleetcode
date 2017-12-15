class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                #if x==y:
                   # continue
                if nums[x]==target-nums[y]:
                    return [x,y]
s=Solution()
print(s.twoSum([3,3],6))