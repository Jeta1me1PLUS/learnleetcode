# Scroll to the bottom for the 3-liner

# An intuitive approach will be to group the binary string into chunks of 0s and 1s (sort of like compressing). The answer will be simply to sum the min of length of neighboring chunks together.

# Here are some examples:

# '00001111' => [4, 4] => min(4, 4) => 4
# '00110' => [2, 2, 1] => min(2, 2) + min(2, 1) => 3
# '10101' => [1, 1, 1, 1, 1] => 4


class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        chunk, consecutive, res = [], 1, 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                consecutive += 1
            else:
                chunk.append(consecutive)
                consecutive = 1
        chunk.append(consecutive)
        # print(chunk)
        sum = 0
        for k in range(len(chunk) - 1):
            sum += min(chunk[k], chunk[k + 1])
        return sum


s = Solution()
print(s.countBinarySubstrings('010001101'))
113211
