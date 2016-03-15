__author__ = 'akamara'
class hashing():
    def __init__(self):
        self.size = 11
        self.slot = [None] * self.size
        self.data = [None] * self.size

    def push(self, key, data):

        current_slot = self.hashfun(key)

        if self.slot[current_slot] == None:
            self.slot[current_slot] = key
            self.data[current_slot] = data

        elif self.slot[current_slot] == key:
            self.data[current_slot] = data

        else:
            while self.slot[current_slot] != None and self.slot[current_slot] != key:
                current_slot = self.rehash(key)

            if self.slot[current_slot] == None:
                self.slot[current_slot] = key
                self.data[current_slot] = data

            elif self.slot[current_slot] == key:
                self.data[current_slot] = data


    def get(self, key):
        slot_found = False
        stop = False

        current_slot = self.hashfun(key)

        if self.slot[current_slot] == key:
            slot_found = True

        else:
            while stop is False and slot_found is False:
                current_slot = rehash(key)
                if self.slot[current_slot] == key:
                    slot_found = True
                elif self.slot[current_slot] == None:
                    stop =  True



    def hashfun(self, key):
        return key % self.size

    def rehash(self, key):
        return (key + 1) % self.size

h = hashing()

h.push(54, "bird")