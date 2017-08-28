"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""
class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class List(object):
    def __init__(self):
        self.sentinel = Node(None, None)
        self.size = 0

    def insert_node(self, node):
        node_to_insert = node
        if self.size == 0:
            # Inserting to empty list
            self.sentinel.next = node_to_insert
            self.sentinel.prev = node_to_insert
            node_to_insert.prev = self.sentinel
            node_to_insert.next = self.sentinel
            self.size += 1
        else:
            # Inserting to non-empty list, insert to front?
            current_head = self.sentinel.next
            self.sentinel.next = node_to_insert
            node_to_insert.prev = self.sentinel
            node_to_insert.next = current_head
            current_head.prev = node_to_insert
            self.size += 1

    def remove_node(self, node):
        if self.size == 0:
            return
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
            self.size -= 1

    def move_node_to_front(self, node):
        self.remove_node(node)
        self.insert_node(node)

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache_size = 0
        self.cache_capacity = capacity
        self.cache = dict()
        self.list = List()

    # Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1

        return_value = self.cache[key].value
        self.list.move_node_to_front(self.cache[key])
        return return_value
    # put(key, value) - Set or insert the value if the key is not already present.
    # When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # Check if capacity
        if key not in self.cache:
            if self.cache_size == self.cache_capacity:
                least_recently_used_key = self.list.sentinel.prev.key
                node_to_delete = self.cache[least_recently_used_key]
                self.list.remove_node(node_to_delete)
                self.cache_size -= 1
                del self.cache[least_recently_used_key]
            node_to_insert = Node(key, value)
            self.list.insert_node(node_to_insert)
            self.cache[key] = node_to_insert
            self.cache_size += 1
        else:
            # nodes need to be inserted
            node_to_insert = Node(key, value)
            self.list.remove_node(self.cache[key])
            self.list.insert_node(node_to_insert)
            self.cache[key] = node_to_insert



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
