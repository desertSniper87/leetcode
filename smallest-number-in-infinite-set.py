import bisect

class SmallestInfiniteSet:
    def __init__(self):
        self.minimum = 1
        self.inifiniteset = []
        

    def popSmallest(self) -> int:
        if self.inifiniteset:
            r = self.inifiniteset.pop(0)
            if r == self.minimum:
                self.minimum += 1
        else:
            r = self.minimum
            self.minimum += 1
        return r
        

    def addBack(self, num: int) -> None:
        if num > self.minimum:
            return

        if num not in self.inifiniteset:
            bisect.insort(self.inifiniteset, num)


obj = SmallestInfiniteSet()

#  cmd = ["SmallestInfiniteSet","addBack","popSmallest","popSmallest","popSmallest","addBack","popSmallest","popSmallest","popSmallest"]
#  val = [[],[2],[],[],[],[1],[],[],[]]
#  cmd = ["SmallestInfiniteSet","popSmallest","popSmallest","addBack","popSmallest","addBack","popSmallest","popSmallest"]
#  val = [[],[],[],[3],[],[2],[],[]]
cmd = ["SmallestInfiniteSet","popSmallest","addBack","popSmallest","popSmallest","popSmallest","addBack","addBack","popSmallest","popSmallest"]
val = [[],[],[1],[],[],[],[2],[3],[],[]]

# cmd = ["SmallestInfiniteSet","popSmallest","addBack","popSmallest","addBack","addBack","popSmallest","popSmallest","popSmallest","addBack","addBack","addBack","addBack","addBack","addBack","addBack","addBack","popSmallest","popSmallest","addBack","popSmallest","addBack","addBack","addBack","popSmallest","popSmallest","popSmallest","addBack","popSmallest","popSmallest","popSmallest","addBack","addBack","addBack","addBack","popSmallest","addBack","addBack","addBack","popSmallest","addBack","addBack","addBack","popSmallest","addBack","popSmallest","addBack","addBack","addBack","popSmallest","popSmallest","popSmallest","popSmallest","addBack","addBack","popSmallest","popSmallest","addBack","popSmallest","addBack","addBack","popSmallest","addBack","addBack","addBack","popSmallest","addBack","popSmallest","popSmallest","popSmallest","popSmallest","addBack","addBack","popSmallest","addBack","popSmallest","popSmallest","popSmallest","addBack","addBack","popSmallest","popSmallest","addBack","popSmallest","popSmallest","addBack","popSmallest","addBack","addBack","popSmallest","addBack","popSmallest","addBack","popSmallest","popSmallest","addBack","addBack","popSmallest","addBack","popSmallest","addBack","popSmallest","addBack","addBack","popSmallest","addBack","addBack","popSmallest","popSmallest","popSmallest","popSmallest","addBack","addBack","addBack","popSmallest","addBack","addBack","popSmallest","addBack","addBack","popSmallest","addBack","popSmallest","popSmallest","popSmallest","popSmallest","addBack","popSmallest","popSmallest","popSmallest","addBack","popSmallest","popSmallest","addBack","popSmallest","popSmallest","popSmallest","addBack","addBack","addBack","addBack","addBack","addBack","popSmallest","popSmallest","addBack","addBack","addBack","addBack","addBack","addBack","addBack","addBack","addBack","addBack","addBack","addBack","addBack","addBack","addBack","popSmallest","addBack","popSmallest","popSmallest","popSmallest","popSmallest","addBack","addBack","popSmallest","addBack","addBack","popSmallest","popSmallest","popSmallest","addBack","popSmallest","addBack","popSmallest","popSmallest","addBack","popSmallest","addBack","popSmallest","popSmallest","addBack","addBack","popSmallest","popSmallest","addBack","addBack","popSmallest","addBack","popSmallest","popSmallest","addBack","addBack","popSmallest","addBack","popSmallest","popSmallest","popSmallest","addBack","popSmallest","addBack","addBack","popSmallest","addBack","addBack","popSmallest","addBack","addBack","popSmallest","popSmallest","addBack","popSmallest","addBack","addBack","addBack","popSmallest","popSmallest","addBack","addBack","addBack","addBack","addBack","addBack","addBack","popSmallest"]
# val = [[],[],[529],[],[779],[732],[],[],[],[494],[907],[641],[226],[194],[182],[532],[477],[],[],[902],[],[564],[61],[301],[],[],[],[924],[],[],[],[591],[988],[653],[607],[],[718],[110],[350],[],[22],[495],[424],[],[328],[],[803],[540],[249],[],[],[],[],[378],[329],[],[],[57],[],[139],[135],[],[479],[869],[424],[],[533],[],[],[],[],[704],[542],[],[602],[],[],[],[235],[851],[],[],[273],[],[],[346],[],[453],[726],[],[609],[],[263],[],[],[507],[38],[],[189],[],[756],[],[652],[736],[],[264],[642],[],[],[],[],[964],[278],[220],[],[695],[76],[],[197],[571],[],[185],[],[],[],[],[293],[],[],[],[890],[],[],[98],[],[],[],[302],[770],[364],[173],[363],[662],[],[],[117],[177],[104],[43],[697],[156],[174],[649],[259],[40],[140],[126],[530],[886],[531],[],[451],[],[],[],[],[452],[542],[],[941],[979],[],[],[],[992],[],[745],[],[],[960],[],[795],[],[],[118],[471],[],[],[226],[458],[],[302],[],[],[264],[114],[],[374],[],[],[],[36],[],[288],[712],[],[629],[449],[],[669],[450],[],[],[184],[],[144],[313],[940],[],[],[645],[249],[591],[31],[43],[941],[898],[]]

for (c, v) in zip(cmd, val):
    match c:
        case 'addBack':
            print(obj.addBack(*v))
        case 'popSmallest':
            print(obj.popSmallest())
        case other:
            pass

