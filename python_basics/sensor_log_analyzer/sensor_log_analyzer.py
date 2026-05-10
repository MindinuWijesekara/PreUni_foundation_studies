file_name = input('Please enter file name with the extention.')
try:
    fhand = open(file_name)
except:
    print('Please ensure file name entered correctly.')
    quit()

counter = 0
for error in fhand:
    error = error.rstrip()
    if 'WARNING' in error and error.startswith('Temp'):
        counter = counter + 1
        print(error)

if counter == 0:
    print('No temperature warnings.')
else:
    print('Number of warning(s) :-',counter)
