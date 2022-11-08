class node:
    def __init__(self,data,next = None ):
        self.data = data
        if next == None:
            self.next = None
        else :
            self.next = next

    def __str__(self):
        return str(self.data)

def createList(l=[]):
    head = node(l[0])
    temp = head
    for i in range(1,len(l)):
        nxt = node(l[i])
        temp.next = nxt
        temp = temp.next
    return head

def printList(H):
    temp = H
    while temp != None:
        print(str(temp),end=" ")
        temp = temp.next
    print()

def mergeOrderesList(p,q):
    if int(p.data) < int(q.data):
        temp = p
        nnP = p.next
        nnQ = q
    else:
        temp = q
        nnP = p
        nnQ = q.next
    head = temp
    while nnP != None or nnQ != None:
        if nnP != None and nnQ != None:
            if int(nnP.data) < int(nnQ.data):
                temp.next = nnP
                temp = temp.next
                nnP = nnP.next
            else:
                temp.next = nnQ
                temp = temp.next
                nnQ = nnQ.next
        elif nnP != None:
            temp.next  = nnP
            temp = temp.next
            nnP = nnP.next
        elif nnQ != None:
            temp.next = nnQ
            temp = temp.next
            nnQ = nnQ.next
    return head




#################### FIX comand ####################   
# input only a number save in L1,L2
l1,l2 = input("Enter 2 Lists : ").split()
L1 = l1.split(",")
L2 = l2.split(",")
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)