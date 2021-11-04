print('This program displays numbers read from a file.')
in_file=open('numbers.txt','r') 
for line in in_file:
    line=line.rstrip()
    print('Number:',line)
in_file.close()


