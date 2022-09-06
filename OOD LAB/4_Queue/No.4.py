'''โรงอาหารของบริษัทแห่งหนึ่ง จะมีเจ้าหน้าที่คอยจัดแถวสำหรับการซื้ออาหาร โดยจะมีหลักการคือจะดูจากแผนกของพนักงานแต่ละคนว่าอยู่แผนกไหน ถ้าหากในแถวที่ต่ออยู่มีแผนกนั้น จะนำพนักงานคนนั้นแทรกไปด้านหลังของแผนกเดียวกัน ตัวอย่างเช่น
Front | 1 2 2 2 2 3 3 3 | Rear  จาก Queue ถ้าหากมีพนักงานแผนก1เข้ามา Queue จะกลายเป็น Front | 1 1 2 2 2 2 3 3 3 | Rear

Input :
จะแบ่งเป็น 2 ฝั่งแบ่งด้วย /   คือ ซ้าย : เป็นแผนกของพนักงานและIDของพนักงานแต่ละคน  ขวา : จะแบ่งเป็น 2 ส่วน คือ D กับ E
E < id >  ->   เป็นการนำพนักงานเข้า Queue
D  ->  เป็นการนำพนักงานคนหน้าสุดออกจากแถว โดยจะแสดงผลเป็น id ของพนักงานคนนั้น ถ้าหากไม่มีพนักงานในแถวจะทำการแสดงผลเป็น Empty'''
class Queue:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def enQueue(self,i):
        self.items.append(i)
    def deQueue(self):
        if len(self.items) > 0:
            return self.items.pop(0)
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def Val(self):
        return self.items
    def AddQ(self,id,m):
        self.temp = []
        for i in range(m):
            self.temp.append(self.items[i])
        self.temp.append(id)
        for i in range(m,len(self.items)):
            self.temp.append(self.items[i])
        self.items = self.temp
    


DPMandID,comm = input("Enter Input : ").split('/')
DPMandID = list(DPMandID.split(','))
comm = list(comm.split(','))
mQ = Queue()
ordQ = Queue()


for i in comm :
    c = i.split()
    if c[0] == 'D':
        if mQ.isEmpty() is False:
            x = mQ.deQueue()
            ordQ.deQueue()
            print(x)
        else:
            print("Empty")
            
    if c[0] == 'E':
        for j in DPMandID:
            data =j.split()
            if data[1] == c[1]:
                dpm = mQ.size()
                for id in range(ordQ.size()-1,-1,-1):
                    if ordQ.Val()[id] == data[0]:
                        dpm = id+1
                        break
                if dpm != mQ.size():
                    mQ.AddQ(data[1],dpm)
                    ordQ.AddQ(data[0],dpm)
                else:
                    mQ.enQueue(data[1])
                    ordQ.enQueue(data[0])



