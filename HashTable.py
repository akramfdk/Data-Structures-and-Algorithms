"""
The code implements a simple hash table
To hand collisions, separate chaining is used
"""

class HashTable:
    def __init__(self, size = 7):
        self.hash_map = [None]*size

    def __hash(self, key):
        """key is a string which is fed to this function to generate its unique hash value between 0 and size - 1
        the value returned by this function is the index at which the key, value pair is stored
        """
        hash_value = 0
        for letter in key:
            hash_value = (hash_value + ord(letter)* 23) % len(self.hash_map)

        return hash_value
    
    def set_value(self, key, value):
        """ this method computes the hash value for the key and gets an index
        The key value pair is stored in the hash_map at this index
        """
        index = self.__hash(key)

        if not self.hash_map[index]:
            self.hash_map[index] = []

        self.hash_map[index].append([key, value])

    def get_value(self, key):
        index = self.__hash(key)
        if self.hash_map[index]:
            for sub_list in self.hash_map[index]:
                if sub_list[0] == key:
                    return sub_list[1]

        return None

    def print_hash_table(self):
        for i, element in enumerate(self.hash_map):
            if element:
                print(i, ":", element)

    def keys(self):
        all_keys = []
        for sublist in self.hash_map:
            if sublist:
                for k,v in sublist:
                    all_keys.append(k)

        return all_keys


my_hash_table = HashTable()
my_hash_table.set_value("Apple", 20)
my_hash_table.set_value("Kiwi", 30)
my_hash_table.set_value("Avocado", 10)
my_hash_table.set_value("Banana", 15)

print(my_hash_table.get_value("Banana"))
print(my_hash_table.get_value("Orange"))
print(my_hash_table.get_value("Apple"))
print(my_hash_table.get_value("Pineapple"))

print("\nHash Table: ")
my_hash_table.print_hash_table()

print("\nKeys: ")
print(my_hash_table.keys())

# print(my_hash_table.hash_map)
