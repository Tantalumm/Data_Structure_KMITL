def hbd(age):
    base = int(age / 2)
    i = int(age % 2)
    if(i == 0):
        s =("saimai is just 20, in base %s!" %base)
    elif(i == 1):
        s =("saimai is just 21, in base %s!" %base)
    return s

year = int(input("Enter year : "))

print(hbd(int(year)))