elmnt_file = input('Enter file name with extention. ')
try:
    fhand = open(elmnt_file)
except:
    print('Error : File not found.!')
    quit()

elmnt_dic = {}
elmnt_list = []
for line in fhand:
    line_list = line.split()
    elmnt_dic[line_list[0]] = line_list[1]
    
for k,v in elmnt_dic.items():
    newtup = v,k
    elmnt_list.append(newtup)

for v,k in sorted(elmnt_list, reverse=True):
    print(k,v)
