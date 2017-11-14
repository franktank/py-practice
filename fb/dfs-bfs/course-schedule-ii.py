class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # Build adjacency list from prerequisites
        # 1 -> 2 in adj list is equivalent to 1 is a prereq for 2
        # [3,5] in prerequisites denotes 5 is a prereq of 3
        adj_list = [[] for i in range(numCourses)]
        prereq_count = [0 for i in range(numCourses)]
        for prereq in prerequisites:
            adj_list[prereq[1]].append(prereq[0])
            prereq_count[prereq[0]] += 1

        res = []
        q = []
        # Enqueue all courses without prereqs
        for i in range(len(prereq_count))
            if prereq_count[i] == 0
                q.append(i)

        while q:
            cur_course = q.pop(0)
            res.append(cur_course)
            for course in adj_list[cur_course]:
                prereq_count[course] -= 1
                if prereq_count[course] == 0:
                    q.append(course)

        if len(res) == numCourses:
            return res
        return []
