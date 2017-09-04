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
    def remove(self, state, prev_i, prev_j, par):
        """
        :type state: str
        :type prev_i: int
        :type prev_j: int
        :type par: [str]
        """
        # prev_i => used to find where last occurence of negative is
        # prev_j => anything before j is valid
        counter = 0
        for i in range(prev_i, len(state)):
            if state[i] == par[0]:
                counter += 1
            if state[i] == par[1]:
                counter -= 1
            if counter < 0:
                for j in range(prev_j, i+1):
                    if state[j] == par[1] and (  or ):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # Have a counter for finding invalid parentheses => ")" first
        # If negative, find respective parentheses to remove
        # Reverse string to find other invalid parentheses => "("
        self.valid_results = list()
        remove(s, 0, 0, ['(', ')'])
        return self.valid_results

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
                # Negative will happen if counter is 0, so return False
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

        # BFS, solutions will be found in a level
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
