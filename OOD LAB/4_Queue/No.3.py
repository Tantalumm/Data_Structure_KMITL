'''จงเขียน ฟังก์ชั่นสำหรับการ encode และ decode ของ String ที่รับมาโดยให้ทำเป็นรูปแบบ Queue

รูปแบบการรับ Input โดยจะคั่นแต่ละตำแหน่งด้วย คอมม่า(',') :

    - ตำแหน่งที่หนึ่ง string ไม่จำกัดความยาวโดยที่จะไม่นับช่องว่าง(spacebar)

    - ตำแหน่งที่สอง ชุดตัวเลข(1-9)

โดยที่รูปแบบการ encode คือ การนำ String ที่รับมาเพิ่มค่า ascii เท่ากับค่าของชุดตัวเลขในตำแหน่งแรก หลังจากนั้นให้ dequeue ชุดตัวเลขออกไปไว้ข้างหลังสุด เช่น ตัวอักษรตำแหน่งแรกคือ i และชุดตัวเลขในตำแหน่งแรกคือ 2 ดังนั้นตัวอักษรที่ได้จากการ encode คือ k โดยจะทำการวนชุดตัวเลขไปเรื่อยๆจนกระทั่งทำการ encode ทุกตัวอักษรใน String ครบ ถ้าหากผลลัพธ์จากการเพิ่มหรือลดค่า ascii ไม่ใช่ตัวอักษรให้กลับมาวนในชุดตัวอักษร เช่น อักษร z ทำการ encode ด้วยเลข 2 จะได้ b และหากทำการ decode ตัวอักษร A ด้วย 2 จะได้ Y 

โดยการ decode หลังจาก encode ต้องให้คำตอบที่มีค่าเท่ากับ String เดิมก่อนทำการ encode 

***ให้ใช้วิธี enqueue และ dequeue ในการเลื่อนตำแหน่ง เท่านั้น***

โดยรูปแบบการ run ดังนี้ :

q1 = Queue(string)

q2 = Queue(number)

encodemsg(q1, q2)

decodemsg(q1, q2)'''

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
    def copy(self,i):
        self.items = i
    

def encodemsg(q1, q2):
    Qencode = []
    Ntemp = q2.items.copy()
    Lnum = Ntemp
    for i in range(q1.size()):
        char = q1.deQueue()
        num = q2.deQueue()
        ascii = ord(char)

        if ascii >= 65 and ascii <= 90:
            if ascii + int(num) > 90:
                ascii += (65 + int(num)) - 91
                ch = chr(ascii)
                Qencode.append(ch)
            else :
                ascii = ascii + int(num)
                ch = chr(ascii)
                Qencode.append(ch)

        elif ascii >= 97 and ascii <= 122:
            if ascii + int(num) > 122:
                ascii += (97 + int(num)) -123
                ch = chr(ascii)
                Qencode.append(ch)
            else :
                ascii = ascii + int(num)
                ch = chr(ascii)
                Qencode.append(ch)

        q2.enQueue(num)
    q1.copy(Qencode)
    q2.copy(Lnum)
    print("Encode message is : ", str(q1.Val()))

def decodemsg(q1, q2):
    Qdecode = []
    Ntemp = q2.items.copy()
    Lnum = Ntemp
    for i in range(q1.size()):
        char = q1.deQueue()
        num = q2.deQueue()
        ascii = ord(char)
        if ascii >= 65 and ascii <= 90:
            if ascii - int(num) < 65:
                ascii -= (90 -(65 - int(num))) +1
                ch = chr(ascii)
                Qdecode.append(ch)
            else :
                ascii = ascii - int(num)
                ch = chr(ascii)
                Qdecode.append(ch)
        elif ascii >= 97 and ascii <= 122:
            if ascii - int(num) < 97:
                ascii -= (122 - (97 - int(num))) + 1
                ch = chr(ascii)
                Qdecode.append(ch)
            else:
                ascii = ascii - int(num)
                ch = chr(ascii)
                Qdecode.append(ch)
        q2.enQueue(num)

    q1.copy(Qdecode)
    q2.copy(Lnum)
    print("Decode message is : " ,str(q1.Val()))

string,number = input("Enter String and Code : ").split(',')

string = string.replace(" ","")

string = list(string)
number = list(number)

q1 = Queue(string)
q2 = Queue(number)

encodemsg(q1, q2)
decodemsg(q1, q2)


