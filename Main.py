from abc import ABC, abstractmethod
from collections import namedtuple
from pyllist import dllist, dllistnode

Point = namedtuple('Point', ['x', 'y', 'z'], defaults=[0,0,0])

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


class LRUCache(Storage):
    maxlen = 0
    fastSaveStorage = dllist()
    fastAccessStorage = dict()
    
    def __init__(self, size = 10):
        self.maxlen = size
        self.fastSaveStorage = dllist()
        self.fastAccessStorage = dict()
        
    @Storage.convert_params
    def put(self, p: Point):
        node = self.fastAccessStorage.get(p,False)
        
        if not node: 
            if len(self.fastSaveStorage) >= self.maxlen:
                self.fastAccessStorage.pop(self.fastSaveStorage.popleft())
                
            self.fastSaveStorage.append(p)
            self.fastAccessStorage[p] = self.fastSaveStorage.last
        else:
            print('{0} already exists!'.format(p))
            
    
    @Storage.convert_params
    def get(self, p: Point):
        elem = Point()
        try:
            elem = self.fastAccessStorage[p]
            self.fastSaveStorage.remove(elem)
            self.fastSaveStorage.append(p)
        except KeyError: 
            print('{0} key not found!'.format(p))
        except ValueError:
            print('{0} node not found!'.format(p))
        except Exception as e:
            print("Some other issue found!",e) 
               
        return elem
        
        
class LFUCache(LRUCache):
    
    fastCountStorage = dict()
    
    def __init__(self):
        self.fastCountStorage = dict()
    
    @Storage.convert_params
    def put(self, p: Point):
        
        node = self.fastAccessStorage.get(p,False)
        
        if not node:                
            self.fastSaveStorage.append(p)
            self.fastAccessStorage[p] = self.fastSaveStorage.last
            self.fastCountStorage[self.fastSaveStorage.last] = 1
        else:
            self.fastCountStorage[node] += 1
     
    def getTopNUsed(self, n):
        return sorted(self.fastCountStorage.items(),key=lambda r: r[1],reverse = True)[:n]     
    
    
    
# --------------------------
p1 = Point(13,13,13)
p2 = Point(2,11,101) 

lru = LRUCache()
lfu = LFUCache()

lru.put(p2)
lru.put(13,13,13)
lfu.put(p2)
lfu.put(13,13,13)

for i in range(5):  # range put
    lru.put(1+i, 10+i, 100+i)
    lfu.put(1+i, 10+i, 100+i)


    lru.get(p1) 
lru.get(p2)

lfu.getTopNUsed(3)
