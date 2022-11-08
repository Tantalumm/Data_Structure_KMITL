class LinkedList :
    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None
            self.prev = None
        
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0

    def indexOf(self,data) :       
        p = self.head
        for i in range(len(self)) :
            if p.data == data :
                return i
            p = p.next
        return -1
            
    def isIn(self,data) :         
        return self.indexOf(data) >= 0

    def nodeAt(self,i) :          
        p = self.head
        for j in range(0,i) :
            p = p.next
        return p

    def append(self,data):           
        if self.head is None :
          p = self.Node(data)
          self.head = p
          self.tail = p
          self.next = None
          self.previous = None
          self.size += 1
        else :                        
          self.insertAfter(len(self)-1,data) 
    
    def insertAfter(self,i,data) :
        if len(self)==0:
            self.addHead(data)   
        else:
            if i<0:
                if(-i>len(self)):
                    i=-1
                else:
                    i=len(self)+i-1
            if i>=len(self):
                i=len(self)-1
            if i==-1:
                self.addHead(data)
            else:
                q = self.nodeAt(i)
                p = self.Node(data)
                if len(self)-1!=i:
                    r = self.nodeAt(i+1)
                    r.previous = p

                p.next = q.next
                q.next = p
                p.previous = q
                
                if i==len(self)-1:
                    self.tail = p
                self.size += 1
    
    def deleteAfter(self,i) :           
        if len(self) > 0 :  
          q = self.nodeAt(i)
          q.next = q.next.next
          self.size -= 1
    
    def deleteHead(self):
        q = self.head.next
        q.previous = None
        self.head = q
        self.size-=1
    
    def removeData(self,data) :          
        if self.isIn(data) :
            self.deleteAfter(self.indexOf(data)-1)
          
    def addHead(self,data) :
        if self.isEmpty() :
            p = self.Node(data)
            self.head = p
            self.tail = p
            self.size += 1
        else :
            q=self.head
            p = self.Node(data)
            q.previous = p
            p.next = q
            self.head = p
            self.size += 1

inp = input("Enter Input : ").split(",")
nowCursor = 0
ll = LinkedList()

for i in inp:
    comm = i.split()
    if comm[0] == "I":
        if(nowCursor != 0):
            ll.insertAfter(nowCursor-1,i[2:])
        else:
            ll.addHead(i[2:])
        nowCursor += 1
    elif comm[0] == "L" and nowCursor > 0 :
        nowCursor -= 1
    elif comm[0] == "R" and nowCursor < len(ll) :
        nowCursor += 1
    elif comm[0] == "B" and nowCursor > 0 :
        nowCursor -= 1
        ll.deleteAfter(nowCursor-1)
    elif comm[0] == "D" and nowCursor < len(ll) :
        if nowCursor == 0 :
            ll.deleteHead()
        else:
            ll.deleteAfter(nowCursor-1)

for i in range(len(ll)):
    if i == nowCursor:
        print('|',end=" ")
    print(ll.nodeAt(i).data,end=" ")
if nowCursor == len(ll):
    print('|',end=" ")