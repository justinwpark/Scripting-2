def main():
    print('This program averages numbers inside a given file.')
    x=input('Enter a filename: ')
    while x!='quit':
        y=average(x)
        print('The average is',format(y,'.2f'))
        x=input('Enter a filename: ')

def average(x):
    in_file=open(x,'r') 
    total=0
    run=0
    for line in in_file:
        run+=1
        line=line.rstrip()
        line=int(line)
        total+=line
    total=total/run
    in_file.close()
    return total

main()
