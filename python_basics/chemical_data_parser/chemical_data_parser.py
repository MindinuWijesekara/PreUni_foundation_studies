entries = input('Enter file name with extension. ')
try:
    fhand = open(entries)
except:
    print('Error : File not found.!')
    quit()

import re
for line in fhand:
    batch = re.findall('^Batch\S[A-Z]:',line)
    formula = re.findall('Formula=([0-9A-Za-z]+)',line)
    if batch and formula:
        print(batch[0]  ,formula[0])
    else:
        print('Error : Entry not compatible.!')
