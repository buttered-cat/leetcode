import sys


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int

        AC;
        linear time
        boundary condition: "", "c"
        """
        max_length = 0
        length = 0
        letters = set()
        head = 0
        tail = 0
        while head < len(s):
            if tail == len(s):
                return max_length
            if s[tail] not in letters:
                length += 1
                letters.add(s[tail])
                tail += 1
                if length > max_length:
                    max_length = length
            else:
                length -= 1
                letters.remove(s[head])
                head += 1

        return max_length


    def run(self):
        seq = sys.stdin.readline().split()[0]
        print(self.lengthOfLongestSubstring(seq))

c = Solution()
c.run()
