import bisect

class SmallestInfiniteSet:
    def __init__(self):
        self.minimum = 1
        

    def popSmallest(self) -> int:
        if self.infiniteSet:
            return self.infiniteSet.pop(0)
        

    def addBack(self, num: int) -> None:
        i = bisect.bisect_left(self.infiniteSet, num)
        if not i:
            self.infiniteSet.insert(i, num)

        


obj = SmallestInfiniteSet()

cmd = ["SmallestInfiniteSet","addBack","popSmallest","popSmallest","popSmallest","addBack","popSmallest","popSmallest","popSmallest"]
val = [[],[2],[],[],[],[1],[],[],[]]

for (c, v) in zip(cmd, val):
    match c:
        case 'addBack':
            print(obj.addBack(v))
        case 'popSmallest':
            print(obj.popSmallest())
        case other:
            pass

