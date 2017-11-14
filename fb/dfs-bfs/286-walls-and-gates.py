class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        # BFS
        # Find all gates first in enqueue
        # Store coordinates
        q = []
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append([i,j])

        while q:
            cur = q.pop(0)
            if rooms[cur[0]+1][cur[1]] == sys.maxint:
                rooms[cur[0]+1][cur[1]] = rooms[cur[0]][cur[1]] + 1
                q.append([cur[0]+1,cur[1]])
            if rooms[cur[0]-1][cur[1]] == sys.maxint:
                rooms[cur[0]-1][cur[1]] = rooms[cur[0]][cur[1]] + 1
                q.append([cur[0]-1,cur[1]])
            if rooms[cur[0]][cur[1]+1] == sys.maxint:
                rooms[cur[0]][cur[1]+1] = rooms[cur[0]][cur[1]] + 1
                q.append([cur[0],cur[1]+1])
            if rooms[cur[0]][cur[1]-1] == sys.maxint:
                rooms[cur[0]][cur[1-1]] = rooms[cur[0]][cur[1]] + 1
                q.append([cur[0],cur[1]-1])
