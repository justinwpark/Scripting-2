def main():
    print('This program prints the contents of files listed in a file.')
    x=input('Enter the file: ')
    early(x)

def early(x):
    try:
        total=0
        in_file=open(x,'r') 
        for line in in_file:
            line=line.rstrip()
            total+=1
        in_file.close()
        if total>1:
            print(total,'files found:')
        else:
            print(total,'file found:')
        in_file=open(x,'r') 
        for line in in_file:
            line=line.rstrip()
            print('\t',line,sep='')
            total+=1
        in_file.close()
        print('')
        opener(x)
    except IOError:
        print('No files found.')

def opener(x):
    in_file=open(x,'r') 
    for line in in_file:
        line=line.rstrip()
        a=opened(line)
    in_file.close()

def opened(x):
    try:
        file=open(x,'r')
        print('Contents of ',x,':',sep='')
        print('')
        for line in file:
            line=line.rstrip()
            print(line)
        file.close()
    except IOError:
        print(x,'does not exist or is an invalid file.')
    print('')
    print('------------------------------')
    print('')

main()
