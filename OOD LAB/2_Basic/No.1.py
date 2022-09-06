class translator:
    def deciToRoman(self,num):
        deci = [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4, 1]
        roman = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV", "I"]
        roman_num = ''
        i = 0
        while  num > 0:
            for x in range(num // deci[i]):
                roman_num += roman[i]
                num -= deci[i]
            i += 1
        return roman_num


    def romanToDeci(self, s):
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        i = 0
        num = 0
        while i < len(s):
         if i+1 < len(s) and s[i:i+2] in roman:
            num+=roman[s[i:i+2]]
            i+=2
         else:
            num+=roman[s[i]]
            i+=1
        return num
                

num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))
print(translator().romanToDeci(translator().deciToRoman(num)))