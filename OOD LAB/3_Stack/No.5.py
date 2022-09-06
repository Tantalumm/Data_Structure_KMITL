'''ที่จอดรถของนาย ก เป็นส่วนที่แรเงาสีฟ้า ส่วนสีแดงเป็นที่ของนาย ข ซี่งเป็นญาติกัน ที่จอดรถของนาย ก และ นาย ข แคบมาก จอดรถได้เรียงเดี่ยว นาย ข ไม่ได้ใช้ที่จอดรถ แต่ อนุญาติให้นาย ก ใช้ที่จอดรถของเขาได้โดยไม่จอดรถแช่ไว้ เนื่องจากซอยแคบ ดังนั้นการมาจอด (arrive) และการรับรถ (depart)จะเป็นลักษณะของ stack เงื่อนไขคือ ในการรับรถ x ใดๆอยากให้ลำดับรถเป็นเหมือนเดิม ดังรูป simulate การจอดรถในที่จอดรถของนาย ก โดยใช้ operation ของ stack ข้างล่างเป็นตัวอย่าง output

การรับ input : รับ input 4 ค่าใน 1 บรรทัดโดยให้แยกโดย " " (space bar) โดยตำแหน่งแรกคือ จำนวนสูงสุดที่รถสามารถจอดได้ในซอยของ นาย ก ตำแหน่งที่สองคือ รถที่จอดอยู่ในซอยของ นาย ก ตำแหน่งที่สามคือ การกระทำเช่น ถ้าเป็น arrive จะทำการเพิ่มรถในซอย ส่วน depart จะทำการเอารถออกจากซอย โดยรถที่จะทำการเพิ่มหรือนำออกนั้นจะเป็น เลขในตำแหน่งที่ 4

***หมายเหตุ ถ้าในซอยไม่มีรถอยู่เลยให้ input = 0 ในตำแหน่งที่ 2***

*** สามารถสร้างได้มากกว่า 1 stack ***

class Stack:

print("******** Parking Lot ********")

m,s,o,n = input("Enter max of car,car in soi,operation : ").split()


m,n = int(m),int(n)

### Enter Your Code Here ###
'''

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
    
    def isEmpty(self):
        return self.items == []
    
    def size(self) :
        return len(self.items)

    def val(self):
        return self.items

print("******** Parking Lot ********")
m,s,o,n = input("Enter max of car,car in soi,operation : ").split()
m,n = int(m),int(n)

suntoiA = Stack()
suntoiB = Stack()

if len(s) == 1 and s[0] == '0':
    s=[]
else :
    s = s.split(',')
    for i in s:
        i = int(i)
        suntoiA.push(i)

if(o == "arrive"):
    if(suntoiA.size() >= m):
        print("car",n,"cannot arrive : Soi Full")
    elif(n in suntoiA.val()):
        print("car",n,"already in soi")
    else:
        suntoiA.push(n)
        print("car",n,"arrive! : Add Car",n)

elif(o == "depart"):
    if(suntoiA.isEmpty() is True):
        print("car",n,"cannot depart : Soi Empty")
    elif(n not in suntoiA.val()):
        print("car",n,"cannot depart : Dont Have Car",n)
    else:
        Dcar =- 1
        while(Dcar != n):
            if suntoiA.isEmpty() is False:
                Dcar = suntoiA.pop()
                if(Dcar == n):
                    print("car",n,"depart ! : Car",n,"was remove")
                    while(suntoiB.isEmpty() is False):
                        suntoiA.push(suntoiB.pop())
                else:
                    suntoiB.push(Dcar)

print(suntoiA)

