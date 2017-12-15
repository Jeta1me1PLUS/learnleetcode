class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(set(candies)), len(candies) / 2)


a = [2, 2, 2, 2, 3, 2]
s = Solution()
b = s.distributeCandies(a)
print(b)
# There are len(set(candies)) unique candies, and the sister picks only len(candies) / 2 of them, so she can't have more than this amount.
# For example, if there are 5 unique candies, then if she is picking 4 candies, she will take 4 unique ones. If she is picking 7 candies, then she will only take 5 unique ones.
