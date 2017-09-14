import sys


class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        AC
        """

        num_count = dict()
        tail_count = dict()
        for n in nums:
            num_count[n] = num_count.get(n, 0) + 1

        for n in nums:
            if num_count.get(n, 0) == 0:
                continue
            elif tail_count.get(n-1, 0) > 0:
                tail_count[n-1] = max(tail_count.get(n-1, 0) - 1, 0)
                tail_count[n] = tail_count.get(n, 0) + 1
            elif num_count.get(n+1, 0) > 0 and num_count.get(n+2, 0) > 0:
                num_count[n+1] = max(num_count.get(n+1, 0) - 1, 0)
                num_count[n+2] = max(num_count.get(n+2, 0) - 1, 0)
                tail_count[n+2] = tail_count.get(n+2, 0) + 1
            else:
                return False

            num_count[n] = max(num_count.get(n, 0) - 1, 0)

        return True

    def run(self):
        print(self.isPossible([1,2,3,3,4,4,5,5]))

c = Solution()
c.run()
