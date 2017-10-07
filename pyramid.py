a=int(input("enter the no of rows"))
for i in range (0,a):
    for j in range (0,a-i):
        print('*',end= ' ')
    for l in range (0,i+1):
        print(end=' ')
    print('\r')   

a=int(input("enter the no of rows"))
for i in range (0,a):
    for j in range (0,a-i):
        print(end='  ')
    for k in range (0,i+1):
        print('VES',end= ' ')
    print('\n')   
num=65
a=int(input("enter the no of rows"))
for i in range (0,a+1):
    for j in range (i):
        ch=chr(num)
        num=num+1
        print(ch,end= ' ')

    print('\r')   


