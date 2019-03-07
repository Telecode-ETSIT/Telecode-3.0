#!/usr/bin/python3

from hashlib import md5
from random import choice, randrange

class Cuckoo():

    def __init__(self, fing_size, bucket_size, table_size, swaps=100):
        self.fings = fing_size
        self.bucks = bucket_size
        self.tabsz = table_size
        self.table = [[]] * table_size
        self.swaps = swaps

    def __contains__(self, item):
        fing = self.fingerprint(item)
        i, j = self.indexes(item)
        return fing in self.table[i] or fing in self.table[j]

    def insert(self, item):
        fing = self.fingerprint(item)
        i, j = self.indexes(item)

        if len(self.table[i]) < self.bucks:
            self.table[i].append(fing)
            return True

        if len(self.table[j]) < self.bucks:
            self.table[j].append(self.fing)
            return True

        idx = choice((i, j))
        for _ in range(self.swaps):
            ridx = randrange(len(self.table[idx]))
            fing, self.table[idx][ridx] = self.table[idx][ridx], fing
            idx = (idx ^ self.index(fing)) % self.tabsz

            if len(self.table[idx]) < self.bucks:
                self.table[idx].append(self.fing)
                return True
        return False

    def remove(self, item):
        fing = self.fingerprint(item)
        (i, j) = self.indexes(item)
        if fing in self.table[i]:
            idx = self.table[i].index(fing)
            del self.table[i][idx]
            return True
        elif fing in self.table[j]:
            idx = self.table[i].index(fing)
            del self.table[i][idx]
            return True
        else:
            return False

    def indexes(self, item):
        fing = self.fingerprint(item)
        idx1 = self.index(str.encode(item))
        idx2 = (idx1 ^ self.index(fing)) % self.tabsz
        return (idx1, idx2)

    def index(self, item):
        h = self.hash(item)
        idx = int.from_bytes(h, "big")
        return idx % self.tabsz

    def fingerprint(self, item):
        h = self.hash(str.encode(item))
        return h[:self.fings]

    def hash(self, item):
        return md5(item).digest()

def read_input():
    N = int(input())
    for i in range(N):
        s = input().split()
        yield (s[0], s[1], i)

res = []
cf = Cuckoo(30000, 500, 2000)

for ins, data, i in read_input():
    if ins == "a":
        cf.insert(data)
    elif ins == "q":
        cf.remove(data)
    elif ins == "b":
        if data in cf:
            res.append(str(i))

print(" ".join(res))
