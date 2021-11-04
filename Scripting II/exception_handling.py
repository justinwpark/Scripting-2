print('This program averages numbers inside a given file.')
x=input('Enter a filename: ')
y='y'
while x!='quit' and y=='y':
    try:
        file=open(x,'r')
        d=0
        total=0
        for line in file:
            line=line.rstrip()
            line=int(line)
            total+=line
            d+=1
        file.close()
        print('The average is',format(total/d,'.2f'))
    except IOError:
        y=input('Error reading from the file. Try again? (y/n): ')
    except ValueError:
        y=input('The file does not have proper numbers. Try again? (y/n): ')
    if y=='y':
       x=input('Enter a filename: ')
    else:
        x='quit'
