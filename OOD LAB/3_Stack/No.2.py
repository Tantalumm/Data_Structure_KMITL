'''จงสร้างฟังก์ชัน ManageStack() ในการจัดการตัวเลขที่อยู่ใน Stack โดยที่จะมีคำสั่งดังนี้

A (add) : ทำการเพิ่มตัวเลขเข้าไปใน Stack

P (pop) : ทำการนำเลขสุดท้ายใน Stack ออก ( ถ้า Stack ว่างให้แสดงผล -1 )

D (delete) : ทำการลบตัวเลขที่ต้องการใน Stack ( ถ้า Stack ว่างให้แสดงผล -1 )  

LD (lessthan delete) : ทำการลบตัวเลขที่น้อยกว่าตัวเลขที่กำหนดทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )

MD (Morethan delete) : ทำการลบตัวเลขที่มากกว่าตัวเลขที่ต้องการทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )

การ Delete ทุกแบบ ถ้าหากไม่มีเลขที่ถูกลบเลย ไม่ต้องแสดงผลอะไรและให้ทำการแสดงผลค่าที่อยู่ใน Stack เมื่อจบโปรแกรม

*** Hint ***

ฟังก์ชัน Delete ต่างๆให้สร้าง Stack ขึ้นมาอีก 1 อันเพื่อใช้เป็น Temp ในการเก็บค่าตัวเลขต่างๆ'''

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
   
    def isEmpty(self):
        return self.items == []
    
    def size(self) :
        return len(self.items)
    
    def copy(self,temp):
        self.items = temp 
    
    def listtoint(self):
        for i in range(len(self.items)):
            self.items[i] = int(self.items[i])
    
        
S = Stack()
order = input("Enter Input : ").split(',')

def delete(num):
    temp1 = Stack()
    if S.isEmpty() is False:
        for i in S.items : 
            if int(i) != int(num) :
                temp1.push(i)
            else :
                print("Delete =",num)
        S.copy(temp1.items)
    else:
        print("-1")

def Ldelete(num):
    tempLD = Stack()
    S.items.reverse()
    if S.isEmpty() is False:
        for i in S.items:
            if int(i) >= int(num) :
                tempLD.push(i)
            else :
                print("Delete =",i,"Because",i,"is less than",num)
        LD = tempLD.items
        LD.reverse()
        S.copy(LD)
    else:
        print("-1")

def Mdelete(num):
    tempMD = Stack()
    S.items.reverse()
    if S.isEmpty() is False:
        for i in S.items:
            if int(i) <= int(num) :
                tempMD.push(i)
            else :
                print("Delete =",i,"Because",i,"is more than",num)
        S.copy(tempMD)
        MD = tempMD.items
        MD.reverse()
        S.copy(MD)
    else:
        print("-1")


for i in order:
    coms = i.split() 
    if coms[0] == 'A':
        S.push(coms[1])
        print("Add =",coms[1])

    elif coms[0] == 'P':
        if S.isEmpty() is False:
            print('Pop =',S.peek()) 
            S.pop()
        else :
            print('-1')

    elif coms[0] == 'D':
        delete(coms[1])

    elif coms[0] == 'LD':
        Ldelete(coms[1])

    elif coms[0] == 'MD':
        Mdelete(coms[1])

S.listtoint()



print("Value in Stack =",str(S.items))

