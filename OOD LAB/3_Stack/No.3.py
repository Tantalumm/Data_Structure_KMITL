class Stack:
    def __init__(self,list = None) :
        if list is None:
            self.items = []
        else : 
            self.items = list

    def push(self, i) :
        return self.items.append(i)

    def pop(self) :
            return self.items.pop()
    
    def isEmpty(self):
        return self.items == []
    
    def size(self) :
        return len(self.items)


Colour = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

inp = input('Enter Input : ').split()

S = Stack()
char = ''
combo = 0
point = 0
for i in inp :
    if i in Colour:
        S.push(i)
    if i == char :
        point+=1
    else :
        char=i
        point = 1
    if point == 3 :
        point = 0
        S.pop()
        S.pop()
        S.pop()
        combo+=1
        if S.size() > 1:
            if S.items[-2] == S.items[-1] :
                char=S.items[-1]
                point = 2
            else :
                char=S.items[-1]
                point = 1
        elif S.size() == 1:
                char=S.items[-1]
                point = 1

print(S.size())


if S.isEmpty() is True: 
    print('Empty',end='')
else:
    S.items.reverse()
    for i in S.items:
        print(i,end='')
    S.items.reverse()

if combo>1 :
    print('\nCombo : '+str(combo)+' ! ! !')

