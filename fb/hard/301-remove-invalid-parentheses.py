"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
"""
# DFS / Backtracking
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

# BFS
# Use a counter to see if parentheses match up
# Use map / filter / reduce
# {} -> dictionary



# Use a counter to see how many number of parantheses to remove
import Queue
class Solution(object):
    def check_validity(self, s):
        """
        :type s: str
        :rtype: Bool
        """
        counter = 0
        for char in s:
            if char == '(':
                counter += 1
            if char == ')':
                if counter == 0:
                    return False
                counter -= 1
        return counter == 0

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        found = False
        valid_results = list()

        q = Queue.Queue()
        seen_states = set()
        q.put(s)

        while not q.empty():
            state = q.get()
            if self.check_validity(state):
                found = True
                valid_results.append(state)

            if found:
                # Only even length valid, next level is odd, so if no more states added, will only have solutions from this level
                continue

            # Create next level of states for current state
            for i in range(len(state)):
                if state[i] == '(' or state[i] == ')':
                    new_state = state[:i] + state[(i+1):]
                    if new_state not in seen_states:
                        q.put(new_state)
                        seen_states.add(new_state)

        return valid_results
