import sys


class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        AC
        """

        points[:] = sorted(points)
        ans = 0
        front = None
        end = None
        while points:
            p = points.pop(0)
            # if front is None:
            #     front = p[0]
            if end is None:
                end = p[1]
                ans += 1

            elif p[0] > end:
                ans += 1
                end = p[1]
            else:
                end = min(end, p[1])

        return ans


    def run(self):
        print(
            self.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]])
        )

c = Solution()
c.run()
