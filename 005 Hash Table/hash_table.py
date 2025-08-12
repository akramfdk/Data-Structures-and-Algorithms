class HashTable:
    def __init__(self, size=7):
        self.data_map = [None]*size

    def _hash(self, key):
        hash_value = 0

        for letter in key:
            hash_value = (hash_value + ord(letter))%len(self.data_map)

        return hash_value
    
    def set_item(self, key, value):
        index = self._hash(key)

        if not self.data_map[index]:
            self.data_map[index] = []

        self.data_map[index].append([key, value])

    
    def get_item(self, key):
        index = self._hash(key)

        if self.data_map[index]:
            for k,v in self.data_map[index]:
                if key == k:
                    return v
        
        return None
    
    def keys(self):
        all_keys = []

        for item_list in self.data_map:
            if item_list:
                for k,_ in item_list:
                    all_keys.append(k)

        return all_keys
    
    def print_hash_table(self):
        for index,item_list in enumerate(self.data_map):
            print(index, end = " -> ")
            if item_list:
                for k, v in item_list:
                    print(f"({k}, {v})", end = " -> ")
            print(None)

ht = HashTable()
ht.print_hash_table()

print("\nSET ITEM")
ht.set_item("bolts", 500)
ht.set_item("nails", 300)
ht.set_item("washers", 750)
ht.set_item("screws", 900)
ht.set_item("hinges", 100)

ht.print_hash_table()

print("\nGET ITEM")
print(ht.get_item("nails"))
print(ht.get_item("hinges"))
print(ht.get_item("pens"))

print("\nKEYS")
print(ht.keys())