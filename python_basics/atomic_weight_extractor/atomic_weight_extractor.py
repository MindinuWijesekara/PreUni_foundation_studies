file_name = input('Enter the file name with extention.')
try:
    fhand = open(file_name)
except:
    print('Please ensure the file name is correct.!')
    quit()

reader = fhand.read()
lister = reader.split()

for value in lister:
    try:
     intv = float(value)
     print(value)
    except:
     continue
