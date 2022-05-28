from random import randrange
import heapq

test_objects = []

def test_object(threshold:int, heapify_objs):
    while heapq.heappop(heapify_objs).strength < threshold-1:
        continue

class MyTestObj:

    strength: int 

    def __init__(self, i:int) -> None:
        self.strength = i

    def __lt__(self, anotherTestObj):
        return self.strength < anotherTestObj.strength

    def __gt__(self, anotherTestObj):
        return self.strength > anotherTestObj.strength
    
    def __str__(self):
        return str(self.strength)



print("Start")
for x in range(10):
    o = MyTestObj(randrange(10))
    print(o)
    test_objects.append(o)

print("heapify & test")
heapq.heapify(test_objects)
test_object(5,test_objects)

print("result")
for o in test_objects:
    print(o)