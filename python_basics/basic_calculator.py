print("Please consider\n  If you're about to use this programme for divition or subtraction please follow the instruction below.\n  For division first number is divident and the second number is divisor.\n  For substraction first number is minuend and the second number is subtrahend.")
a = input('Enter your first number :- ')
b = input('Enter your second number :- ')
c = input('Please select an arithmetic operator \n + for ADDITION\n - for SUBTRACTION\n * for MULTIPLICATION\n / for DIVISION\n Operator is ')
if b == '0' and c == '/':
  print('Error : division by zero.!')
else:
 a2 = float(a)
 b2 = float(b)
 def number(a2,b2,c):
    if c == '+':
        result = a2 + b2
        return result
    if c == '/':
        result = a2/b2
        return result
    if c == '*':
        result = a2*b2
        return result
    if c == '-':
        result = a2-b2
        return result
    else:
        return 'having a trouble displaying.!'

 print('Your answer is',number(a2,b2,c))
