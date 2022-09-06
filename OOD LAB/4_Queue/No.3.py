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


