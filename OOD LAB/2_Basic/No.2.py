class Bus:
    def __init__(self,people, fare):
        self.people = people
        self.fare = fare
        self.sum = self.people * self.fare
    def __str__(self):
        return 'this bus has ' + str(self.people) + ' people with fare = ' + str(self.fare)
    def __lt__(rhs,sum):
        return sum < rhs.people*rhs.fare
    def people_in(pi,k):
        pi.people += k   
    def people_out(po,k):
        po.people -= k
        if(po.people <= 0):
            po.people = 0
    def change_fare(mfare,new_fare):
        mfare.fare = new_fare


b1, b2, f1, f2 = input("Enter people in Bus1, Bus2, fare Bus1, Bus2 : ").split()
b1 = Bus(int(b1), int(f1))
b2 = Bus(int(b2), int(f2))
if b1 < b2:
    print(b1)
else:
    print(b2)
b1.people_in(3)
b1.people_out(6)
b1.change_fare(12)
print(b1)

