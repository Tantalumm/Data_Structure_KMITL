class DoublyLinkedList:
    class Node:
        def __init__(self,data,prev = None,next = None):
            self.data = data
            if prev == None:
                self.next = None
            else:
                self.prev = prev
            if next == None:
                self.prev = None
            else:
                self.next = next

    def __init__(self):
        self.head = self.Node(None,None,None)
        self.head.next = self.head.prev = self.head
        self.size = 0 
    
    def __len__(self) :
        return self.size
    
    
    def isEmpty(self):
        return self.size == 0
    
    def indexOf(self,data):
        temp = self.head.next
        for i in range(len(self)):
            if temp.data == data:
                return i
            temp = temp.next
        return -1

    def isIn(self,data):
        return self.indexOf(data) >= 0

    def nodeAt(self,pos):
        temp = self.head
        for i in range(-1,pos):
            temp = temp.next
        return temp
    
    def append(self,data):
        self.insert(self.nodeAt(len(self)),data)

    def insert(self,index,data):
        p = index.prev
        temp = self.Node(data,p,index)
        p.next = index.prev = temp
        self.size += 1
    
    def remove(self,data):
        if self.isIn(data):
            data = self.nodeAt(self.indexOf(data))
            p = data.prev
            n = data.next
            p.next = n
            n.prev = p
            self.size -= 1 
            return data

        else:
            return -1

    def delete(self,index):
        self.remove(self.nodeAt(index))
    
    def __str__(self) :
        s = ''
        p = self.head.next
        for i in range(len(self)-1):
            s += str(p.data) + '->'
            p = p.next
        if str(p.data) != "None":
            s += str(p.data)
        return s
    
    
    def str_reverse(self) :
        s = ''
        p = self.nodeAt(len(self)-1)
        for i in range(len(self)-1):
            s += str(p.data) + '->'
            p = p.prev
        if str(p.data) != "None":
            s += str(p.data)
        return s


Dl = DoublyLinkedList()

inp = input("Enter Input : ").split(",")

for i in inp :
    comm = i.split()
    if comm[0] == "A":
        Dl.append(comm[1])
    elif comm[0] == "Ab":
        Dl.insert(Dl.nodeAt(0),comm[1])
    elif comm[0] == "I":
        i,d = comm[1].split(":")
        if int(i) < 0 or len(Dl) < int(i):
            print("Data cannot be added")
        else:
            Dl.insert(Dl.nodeAt(int(i)),d)
            print("index = {0} and data = {1}".format(i,d))
    elif comm[0] == "R":
        i = Dl.indexOf(comm[1])
        r = Dl.remove(comm[1])
        if r == -1:
            print("Not Found!")
        else:
            print("removed : {0} from index : {1}".format(str(r.data),str(i)))

    
    print("linked list :",str(Dl))
    print("reverse :",Dl.str_reverse())
    