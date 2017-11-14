"""
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function may be called multiple times.
"""
# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    self.buffer_pointer = 0
    self.buffer_counter = 0
    self.buffer = [None for _ in range(4)]

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        counter = 0
        while(counter < n):
            if self.buffer_pointer == 0:
                read4(self.buffer)
            if self.buffer_counter == 0:
                break
            while counter < n and self.buffer_pointer < self.buffer_counter:
                self.buffer[counter += 1] = self.buffer[self.buffer_pointer += 1]

            if self.buffer_pointer >= self.buffer_counter:
                self.buffer_pointer == 0
        return counter
