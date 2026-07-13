class LinkedList:
    
    def __init__(self):
        self.l=[]

    
    def get(self, index: int) -> int:
        if index in range(len(self.l)):

            return self.l[index]
        return -1
        

    def insertHead(self, val: int) -> None:
        self.l.insert(0,val)

    def insertTail(self, val: int) -> None:
        self.l.append(val)

    def remove(self, index: int) -> bool:
        if index in range(len(self.l)):
            self.l.remove(self.l[index])
            return True
        return False

    def getValues(self) -> List[int]:
        return self.l
