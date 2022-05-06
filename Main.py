from abc import ABC, abstractmethod
from collections import namedtuple
from pyllist import dllist, dllistnode

# base definition of Point
Point = namedtuple('Point', ['x', 'y', 'z'], defaults=[0,0,0])

# base class for different storages
class Storage(ABC):
    
    @staticmethod
    def convert_params(fn):
        def wrap_func(*args, **kwargs):
            if(len(args)>2):
                (s,x1,x2,x3) = args
                p = Point(x1,x2,x3)
            elif(len(args)>1):
                (s,p) = args
            return fn(s,p)
        return wrap_func
    
    @abstractmethod
    def get(self, *args, **kwargs) -> Point:
        pass    
    
    @abstractmethod
    def put(self, *args, **kwargs):
        pass

# class for Last 10 used (with duplicates)
class LRUCache(Storage):
    
    def __init__(self, size = 10):
        self.maxlen = size
        self.storage = dllist()
        
    @Storage.convert_params
    def put(self, p):
        if len(self.storage) >= self.maxlen:     # O(1)
            self.storage.popleft()               # O(1)
        self.storage.append(p)                   # O(1)
            
    @Storage.convert_params
    def get(self, p):
        if p not in self.storage:                # O(n)
            print('{0} not found!'.format(p))          
        else:
            return p
        

# class for Top 10 frequently used
class LFUCache(Storage):
    
    def __init__(self):
        self.storage = dict()
    
    @Storage.convert_params
    def put(self, p: Point):
        self.storage[p] = self.storage.setdefault(p,0)+1
     
    def get(self, n):
        return sorted(self.storage.items(),key=lambda kv:(kv[1],kv[0]),reverse = True)[:n]     
    
    
    
    
    
    
    
# --------------------------
p1 = Point(13,13,13) # custom point (not from range put)
p2 = Point(2,11,101) # point from range put

lru = LRUCache()
lfu = LFUCache()
lfu.put(p1)
lfu.put(13,13,13)

for i in range(10):  # range put
    lru.put(1+i, 10+i, 100+i)

lru.get(p1) # get custom not-existing point
lru.get(p2) # get existing point from range put

lfu.storage
