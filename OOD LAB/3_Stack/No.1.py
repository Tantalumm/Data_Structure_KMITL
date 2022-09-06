class Stack:
    def __init__(self,list = None) :
        if list is None:
            self.items = []
        else : 
            self.items = list 
        
    def __str__(self) :
        return str(self.items)
    
    def push(self, i) :
        return self.items.append(i)

    def pop(self) :
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def lastindex(self):
        return len(self.items)-1
    
    def isEmpty(self):
        return self.items == []
    
    def size(self) :
        return len(self.items)


order = list(input("Enter Input : ").split(','))

stk = Stack()

for i in range(len(order)):
    coms = order[i]
    if coms[0] == 'A':
        coms,word = order[i].split()
    else :
        coms = order[i][0]
        word = ''
    
    if coms == 'A':
        stk.push(word)
        print('Add =',word,'and','Size =',stk.size())
    
    elif coms == 'P':     
        if stk.isEmpty() is False:
            print('Pop =',stk.peek(),'and','Index =',stk.size()-1)
            stk.pop()
        else:
            print('-1')
            continue

if stk.isEmpty() is True:
    print("Value in Stack = Empty")

else :
    print("Value in Stack =",end=' ')
    for j in range(len(stk.items)):
        print(stk.items[j],end=' ')