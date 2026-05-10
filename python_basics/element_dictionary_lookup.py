element = {'H':1.008,'C':12.011,'O':15.999,'N':14.007,'F':18.998,'Na':22.990}
name = input('Please enter the element ')

x = element.get(name,'Element not found.!')
if name in element:
 print('Atomic weight of',name,'is',x)
else:
 print(x)
