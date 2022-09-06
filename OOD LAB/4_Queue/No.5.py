class Queue:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
            
    def enQueue(self,i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)

    def deRearQueue(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def Val(self):
        return self.items
    
def CP(lcc):
    q = Queue()
    List = lcc
    List.reverse()
    index = 2
    num = 0
    while index < len(List):
        if List[index] == List[index-1] and List[index-1] == List[index-2]:
            q.enQueue(List[index])
            List.pop(index-2)
            List.pop(index-2)
            List.pop(index-2)
            index = 2
            num += 1
        else:
            index += 1
    q.enQueue(num)
    return q

def RAP(lcc):
    q = Queue()
    List = lcc
    List.reverse()
    index = 2
    num = 0
    while index < len(List):
        if List[index] == List[index-1] and List[index-1] == List[index-2]:
            List.pop(index-2)
            List.pop(index-2)
            List.pop(index-2)
            index = 2
            num += 1
        else:
            index += 1
    for i in List:
        q.enQueue(i)
    q.enQueue(num)
    return q

def Inplist(data,list = list):
    for i in range(len(data)):
        list.append(data[i])

def displayNM(size,Val,Combo,fail):
    print("NORMAL :\n"+str(size))
    if(size != 0):
        for i in Val:
            print(i,end="")
        print("")
    else:
        print("Empty")
    print(str(Combo)+" Explosive(s) ! ! ! (NORMAL)")
    if fail != 0:
        print("Failed Interrupted "+str(fail)+" Bomb(s)")

def displayMR(size,Val,Combo):
    print("------------MIRROR------------")
    print(": RORRIM")
    print(size)
    if(size!=0):
        for i in Val:
            print(i,end="")
        print("")
    else:
        print("ytpmE")
    print("(RORRIM) ! ! ! (s)evisolpxE "+str(Combo))
        
Nm,Mr = input("Enter Input (Normal, Mirror) : ").split()
Normal = []
Mirror = []
TempNormal = []

Inplist(Nm,Normal)
Inplist(Mr,Mirror)
    
q = CP(Mirror)
finalMr = RAP(Mirror)
finalMr.deRearQueue()
MRcombo = q.deRearQueue()
point = 0
failed = 0
temp = Normal[0]
for i in Normal:
    if i==temp :
        point += 1
    else :
        temp = i
        point = 1
    if point==3 and q.size()!=0:
        item = q.deQueue()
        if i==item:
            failed += 1
        TempNormal.append(item)
        point = 0
    elif point == 3:
        point = 0
    TempNormal.append(i)
final = RAP(TempNormal)

NMcombo = final.deRearQueue()

SMcombo = NMcombo - failed

displayNM(final.size(),final.Val(),SMcombo,failed)
displayMR(finalMr.size(),finalMr.Val(),MRcombo)

