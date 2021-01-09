x = input("Введите набор символов (+,-,*,/): ")
a=x.find('+')
b=x.find('-')
c=x.find('*')
d=x.find('/')
if a>1:
    print(a)
elif b>1:
    print (b)
elif c>1:
    print (c)
elif d>1:
    print (d)
