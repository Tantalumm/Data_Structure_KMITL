'''จำลองการเลื่อนแถวคอยภายในเวลาที่กำหนดโดยใช้ class queue

โดยที่มีแถวหลัก 1 แถวยาวกี่คนก็ได้

แถวหน้า cashier 1 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 3 นาทีในการคิดค่าบริการ

แถวหน้า cashier 2 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 2 นาทีในการคิดค่าบริการ

ลูกค้าจะ move แถวทุกๆ 1 นาที โดยหากแถว 1 ว่างจะไปก่อนหากเต็มจึงไปแถว 2

จงแสดง นาที [แถวหลัก] [แถว cashier 1] [แถว cashier 2]

'''
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
    def isfull(self):
        if len(self.items) >= 5:
            return True
        else:
            return False
        
people,Mtime = input("Enter people and time : ").split()
Mp = list(people)
cq1 = Queue()
cq2 = Queue()
cq3 = Queue()
Mtime = int(Mtime)
time,time1,time2 = 0,0,0

for i in people: 
    cq3.enQueue(i)

for time in range(1, Mtime+1):
    print(time,end=' ')

    if time1 >= 3 and not cq1.isEmpty():
        cq1.deQueue()
        time1 = 0
    if time2 >= 2 and not cq2.isEmpty():
        cq2.deQueue()
        time2 = 0

    if cq1.isfull() is False and not cq3.isEmpty():
            cq1.enQueue(cq3.deQueue())
    elif cq2.isfull() is False and not cq3.isEmpty() :
            cq2.enQueue(cq3.deQueue())
            
   
    if cq1.isEmpty() is False :
        time1 += 1
    if cq2.isEmpty() is False:
        time2 += 1
    print(cq3.Val(),end=' ')
    print(cq1.Val(),end=' ')
    print(cq2.Val())






