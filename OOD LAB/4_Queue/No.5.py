'''เกม Color Crush คืออะไร : Color Crush จะเป็นเกมที่นำสีมาเรียงต่อกัน โดยสีจะหายไปก็ต่อเมื่อมีการเรียงสีเหมือนกันครบ 3 อัน เช่น  ABBBA  -> AA  เนื่องจาก B เรียงติดกัน 3 ตัวทำให้ระเบิดหายไปโดยที่สีจะมีทั้งหมด 26 สี และจะถูกแทนด้วย A - Z  ถ้าหากมีการเรียงกันแบบ  ABBBAA -> Empty  เนื่องจาก  ถ้าหาก B ระเบิด  A(BBB)AA -> AAA จะเห็นว่า A ก็เรียงกันอีก 3 ตัวทำให้เกิดการระเบิดขึ้นอีกครั้งหนึ่ง  และถ้าหากมีการเรียงกันแบบ AAAA -> A เนื่องจากมีการเรียงกัน 3 ตัว  (AAA)A ทำให้เหลือ A 1 ตัว



เนื้อเรื่อง :    หลังจากที่กฤษฎาได้เล่นเกม Color Crush ก็ได้ไปเห็นโฆษณาว่า บริษัทที่ได้สร้าง Color Crush มีแผนการที่จะสร้างเกม Color Crush 2 ขึ้นมา 
            กฤษฎาจึงได้สมัครเข้าไปร่วมทีมในการสร้างเกม Color Crush 2 ซึ่งเกมนี้จะมีกิมมิคที่แตกต่างออกไป คือการที่จะมี 2 ฝั่ง คือ ฝั่งปกติกับฝั่งโลกกระจก 
            โดยฝั่งโลกกระจกจะเกิดการระเบิดก่อน ซึ่งการระเบิดของฝั่งโลกกระจกจะไม่ใช่ระเบิดแล้วหายไปเลย แต่จะเป็นระเบิดแล้วกลายเป็น ITEM ไว้สำหรับขัดขวางการระเบิดของฝั่งปกติ  
            หลังจากที่ฝั่งโลกกระจกเกิดการระเบิดครบแล้ว ก็จะเป็นคิวของฝั่งปกติ  ซึ่งถ้าหากฝั่งปกติมีการเรียงกันของสีที่จะทำให้เกิดการระเบิด ในเสี้ยววินาทีนั้นก่อนที่จะเกิดการระเบิดของฝั่งปกติ  
            ITEM สำหรับขัดขวางการระเบิดของฝั่งโลกกระจก จะมาคั่นระหว่างระเบิดลูกที่ 2 กับ ลูกที่ 3 (อาจจะทำให้เกิดการระเบิดเหมือนเดิมได้ถ้าหาก ระเบิดนั้นเป็นสีเดียวกัน  แต่ถ้าเป็นคนละสีก็จะทำให้ไม่เกิดการระเบิดขึ้น)  โดยระเบิดอาจจะเกิดการระเบิดซ้อนๆกันเรื่อยๆได้จะเป็น Empty  เช่น ถ้าหากฝั่งปกติมีระเบิดเรียงแบบนี้ AAAAA และฝั่งโลกกระจกมีระเบิดแบบนี้ AAA ถ้าหากฝั่งปกติระเบิดธรรมดา 1 ทีจะเหลือแค่ AA แต่ถ้าหากฝั่งโลกกระจกมาขัดขวาง จะกลายเป็น AA(A)AAAA ก็จะเกิดระเบิด 2 ทีทำให้ระเบิดฝั่งปกติเป็น Empty

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

