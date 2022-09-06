print("*** Reading E-Book ***")

text, hl = input("Text , Highlight : ").split(",")

for n in range(len(text)):
    if(text[n] is hl ):
        print('[%s]' %text[n],end='')
    else:
        print(text[n],end='')


