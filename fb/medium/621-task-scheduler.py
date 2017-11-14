"""
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ['A','A','A','B','B','B'], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = {}
        unique_tasks = []
        res = []
        for task in tasks:
            if task in counter:
                counter[task] += 1
            else:
                counter[task] = 1
                unique_tasks.append(task)
        g = 0
        while counter:
            res.append(unique_tasks[g])
            counter[unique_tasks[g]] -= 1
            if counter[unique_tasks[g]] == 0:
                del counter[unique_tasks[g]]
                if not counter:
                    break
                else:
                    g += 1
                    # if g == len(unique_tasks):
                    #     break
            temp_n = n
            for u in unique_tasks:
                if u == g:
                    continue
                if u in counter:
                    res.append(u)
                    counter[u] -= 1
                    if counter[u] == 0
                        del counter[u]
                    temp_n -= 1
                if temp_n == 0:
                    break

            while not temp_n == 0:
                list.append(None)
                n -= 1
            res.append(counter[g])
