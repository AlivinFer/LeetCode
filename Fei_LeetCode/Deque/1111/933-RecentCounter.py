"""
感觉像是做了一题阅读理解
题目的意思是只考虑当前时刻，以及当前时刻前3000ms内ping的次数
所给的例子  input [[], 1, 100, 3001, 3002]
          output [null, 1, 2, 3, 3]
时刻 1 ping 指的是 当前时刻 1 以及 1 之前的3000ms，即-2999-1 所以仅1时刻ping了一次
时刻 100 ping 指的是 当前时刻 100 以及 100之前的3000ms，即-2900-100，包括 1 时刻 & 100 时刻
...
"""
import collections
class RecentCounter(object):
    def __init__(self):
        self.stack = collections.deque()

    def ping(self, t: int):
        """用双端队列来实现"""
        self.stack.append(t)
        while self.stack[0] < t-3000:
            self.stack.popleft()
        return len(self.stack)
