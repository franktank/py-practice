"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # How to handle loops?
        
        # To take a course, we must have its prerequisite done
        # Brute Force
            # For each course we see, try to find if its preqrequisite can be done
                # Iterate through rest of prerequisites:
                    # If it is NOT in preqrequisites
                        # The preqrequisite can be finished, and then numCourses -= 1

                    # If it is in prerequisites, repeat and make it None in prerequisites if it can be done, and then numCourses -= 1

        for pr in prerequisites:
            if pr == None:
                continue
            take = self.helper(pr, prerequisites)
            if take:
                numCourses -= 1
                if numCourses < 0:
                    return False
            else:

        return True

    def helper(self, pr, prerequisites):
        """
        :rtype: bool
        """
        for pr in prerequisites
