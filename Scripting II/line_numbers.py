x=input('Enter a filename: ')
print('')
print('Contents of',x)
total=0
in_file=open(x,'r')
for line in in_file:
    line=line.rstrip()
    total+=1
    print(total,':\t',line,sep='')
in_file.close()


