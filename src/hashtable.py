import hashlib

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    """

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        """
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        """
        return hash(key)

    def _hash_djb2(self, key):
        """
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        """
        pass

    def _hash_mod(self, key):
        """
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        """
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        """
        index = self._hash_mod(key)
        # check if there is an item already
        if self.storage[index] is not None:
            # create node
            new_node = LinkedPair(key, value)
            # make the current index value the next value of the new node
            new_node.next = self.storage[index]
            # make new node be the new current value for index
            self.storage[index] = new_node
        else:
            # if there isn't, assign node
            self.storage[index] = LinkedPair(key, value)

    def remove(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        """
        index = self._hash_mod(key)
        node = self.storage[index]
        if node is None:
            return "ERROR: No Key found"
        else:
            while node is not None and node.key != key:
                if node.next:
                    node = node.next
                else:
                    node.value = None
                    return
            return node

    def retrieve(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        """
        index = self._hash_mod(key)
        node = self.storage[index]
        while node is not None and node.key != key:
            if node.next:
                node = node.next
            else:
                return None
        return node.value

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        """
        # capture old storage
        old_storage = self.storage
        self.capacity *= 2
        # overwrite current storage with None values
        self.storage = [None] * self.capacity
        # replace with old storage values + None
        for bucket_item in old_storage:
            if bucket_item is not None:

                self.insert(bucket_item.key, bucket_item.value)
            else:
                self.insert(None, None)


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))
    print(ht.retrieve("line_4"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
