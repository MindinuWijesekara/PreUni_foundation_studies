lowest = None
highest = None
counter = 0
sumofph = 0
while True:
    p_H = input('Enter your next reading or type "DONE" to end. ')
    if p_H == 'DONE':
        break
    else:
        pH = float(p_H)
        counter = counter + 1
        sumofph = sumofph + pH

        if lowest is None:
            lowest = pH
        elif lowest > pH:
            lowest = pH

        if highest is None:
            highest = pH
        elif highest < pH:
            highest = pH

if counter > 0:
 print('Your total number of readings is',counter)
 print('Your highest pH is',highest)
 print('Your lowest pH is',lowest)
 print('Your average pH is',sumofph/counter)
else:
    print('No readings were entered.!')
