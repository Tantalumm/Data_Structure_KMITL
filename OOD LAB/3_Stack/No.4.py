'''ให้เขียน class calculator  ที่มีการทำงานผ่านฟังก์ชัน run(instructions) โดยมี instructions ดังนี้
+: Pop 2 ค่าออกจาก stack, นำมาบวกกัน และ push ผลลัพธ์ลง stack
-: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนลบด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
*: Pop 2 ค่าออกจาก stack, นำมาคูณกัน และ push ผลลัพธ์ลง stack
/: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนหารด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
DUP: Duplicate (not double) ค่าบนสุดของ stack
POP: Pop ค่าบนสุดออกจาก stack และ discard.
PSH: ทำการ push ตัวเลขลง stack
หมายเหตุ คำสั่งอื่น ๆ (เช่นตัวอักษร) ควรทำให้เกิดค่า "Invalid instruction: [instruction]"
*************************************************
print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())'''

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


class StackCalc():
    def __init__(self):
        self.result = 0
    def run(self,inp):
        arg = inp.split()
        self.result = Calculator(arg)
        if self.result == '' :
            self.result = 0
    def getValue(self):
        return self.result


def Calculator(stack):
    S = Stack()
    for i in stack:
        if i == '+':
            x = S.pop()
            y = S.pop()
            result = x+y
            S.push(result)
        elif i == '-':
            x = S.pop()
            y = S.pop()
            result = x-y
            S.push(result)
        elif i == '*':
            x = S.pop()
            y = S.pop()
            result = x*y
            S.push(result)
        elif i == '/':
            x = S.pop()
            y = S.pop()
            result = x/y
            S.push(result)
        elif i == "DUP":
            x = S.pop()
            S.push(x)
            S.push(x)   
        elif i == "POP":
            S.pop()
        elif i == "PSH":
            S.push()
        elif i.isalpha():
            return "Invalid instruction: "+i
        else:
            S.push(int(i))
    if S.isEmpty() is False:
        return int(S.pop())
    else:
        return 0
            


print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())
