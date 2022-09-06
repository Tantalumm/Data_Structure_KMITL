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
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def Val(self):
        return self.items
    def peek(self):
        return self.items[-1]

order = list(input("Enter Input : ").split(','))

q = Queue()

for i in range(len(order)):
    coms = order[i]
    if coms[0] == 'E':
        coms,num = order[i].split()
    else :
        coms = order[i][0]
        num = 0
    
    if coms == 'E':
        q.enQueue(num)
        print('Add',num,'index is',q.size()-1)
    
    elif coms == 'D':     
        if q.isEmpty() is False:
            print('Pop',q.deQueue(),'size in queue is',q.size())
            
        else:
            print('-1')
            continue

if q.isEmpty() is True:
    print("Empty")

else :
    print("Number in Queue is :",end='  ')
    print(q.items,end=' ')


