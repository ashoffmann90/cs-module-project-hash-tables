class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class LinkedList:
    def __init__(self):
        self.head = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.size = 0
        self.buckets = [LinkedList()] * capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.buckets)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.

        *number of slots used / number of total slots
        """
        # Your code here
        return self.size/len(self.buckets)

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        # Your code here
        pass

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # find the index
        index = self.hash_index(key)
        # if there is nothing there
        if self.buckets[index].head is None:
            # put it here
            self.buckets[index].head = HashTableEntry(key, value)
            self.size += 1
        else:
            # set your current position
            cur = self.buckets[index].head
            # while there is a next node
            while cur.next:
                # and if the current position is the same as the passed in key
                if cur.key == key:
                    cur.value = value
                cur = cur.next

            cur.next = HashTableEntry(key, value)
            self.size += 1

        # day one's homework
        # # Your code here
        # # find the key
        # index = self.hash_index(key)
        # # if there is nothing there
        # if self.buckets[index] is None:
        #     # create a new node
        #     self.buckets[index] = HashTableEntry(key, value)
        #     # increment to indicate we added a node
        #     self.size += 1
        # # otherwise
        # else:
        #     # set your position to the first item
        #     item = self.buckets[index]
        #     # if the key at that position is the same as the key passed in
        #     if item.key == key:
        #         # set the item's value to the value passed in
        #         item.value = value
        #     # otherwise
        #     else:
        #         # while the next item is not the last element AND the item is not the same as the passed in key
        #         while item.next != None and item.key != key:
        #             # move your position to the next item
        #             item = item.next
        #         # after you exit the loop, set the next item to the newly created node
        #         item.next = HashTableEntry(key, value)
        #         # and increment
        #         self.size += 1

        # code that didn't work?
        # # increment so that we know we added an element
        # # find the index we're going to in array, by using hash function we created
        # self.size += 1
        # index = self.hash_index(key)
        # # find the item at that index
        # item = self.buckets[index]
        # # if the bucket is empty, create a new node and add it to that bucket
        # if item is None:
        #     self.buckets = HashTableEntry(key, value)
        #     return
        # # if a collision occurs (there is an item already there), iterate to end and add key there
        # # we have to keep track of the prev and current item
        # prev = item
        # while item is not None:
        #     # moves to the next item
        #     prev = item
        #     item = item.next
        # prev.next = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here

        index = self.hash_index(key)
        item = self.buckets[index].head

        if item.key == key:
            self.buckets[index].head = self.buckets[index].head.next
            self.size -= 1
            return

        while item.next:
            prev = item
            item = item.next
            if item.key == key:
                prev.next = item.next
                self.size -= 1
                return None

        # day one's code
        # index = self.hash_index(key)
        # item = self.buckets[index]
        # if self.buckets[index].key == key:
        #     self.buckets[index] = None
        #     self.size -= 1
        # elif self.buckets[index].key != key and self.buckets[index].next != None:
        #     prev = self.buckets[index]
        #     current = self.buckets[index].next
        #     while current.key != key and current.next != None:
        #         prev, current = current, current.next
        #     if current.key == key:
        #         prev.next = current.next
        #         self.size -= 1
        # if self.buckets[index] == None:
        #     print('Key does not exist.')

        # while item is not None and item.key != key:
        #     prev = item
        #     item = item.next
        # if item is None:
        #     return None
        # else:
        #     self.size -= 1
        #     result = item.value
        #     if prev is None:
        #         item = None
        #     else:
        #         prev.next = prev.next.next
        #     return result

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        item = self.buckets[index].head
        if item == None:
            return None
        if item.key == key:
            return item. value

        while item.next:
            item = item.next
            if item.key == key:
                return item.value
        return None

        # yesterday's, switch this while with the previous while
        # while item.key != key and item.next != None:
        #     item = item.next

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        self.capacity = new_capacity
        new_list = [LinkedList()] * new_capacity

        for i in self.buckets:
            cur = i.head

            while cur is not None:
                index = self.hash_index(cur.key)

                if new_list[index].head == None:
                    new_list[index].head = HashTableEntry(cur.key, cur.value)
                else:
                    item = HashTableEntry(cur.key, cur.value)
                    item.next = new_list[index].head
                    new_list[index].head = item
                cur = cur.next
        self.buckets = new_list


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
