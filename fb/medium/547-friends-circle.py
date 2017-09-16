"""
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:
Input:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.
"""
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # Like number of islands?
        number_groups = 0
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    number_groups += 1
                    self.check_adjacent(M, row, col)
        return number_groups

    def check_adjacent(self, M, row, col):
        # Check border cases
        if row < 0 or row >= len(M) or col < 0 or col >= len(M[0]):
            return
        if M[row][col] == 0:
            return
        M[row][col] = 0
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                # not diagonals
                if (i == row - 1 and j == col) or (i == row + 1 and j == col) or (i == row and j == col - 1) or (i == row and j == col + 1):

                    self.check_adjacent(M, i, j)

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        visited = [0 for _ in range(len(M))]
        number_groups = 0
        for i in range(len(M)):
            if visited[i] == 0:
                number_groups += 1
                visited[i] = 1
                self.dfs(M, visited, i)
        return number_groups

    def dfs(self, M, visited, i):
        for j in range(len(M)):
            # Visit all directed, directed will visit all indirected related to this friend
            if M[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                self.dfs(M, visited, j)
