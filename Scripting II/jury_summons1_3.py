def main():
    print('This program divides a group of people into jury pools.')
    x=input('Enter a file name: ')
    y=int(input('Enter a number: '))
    a=verify_file(x,y)
    if a==True:
        print('File is OK.')
    else:
        print('There was a problem with the file:',x)
    
def verify_file(filename,number):
    try:
        total=0
        file=open(filename,'r')
        for line in file:
            line=line.rstrip()
            total+=1
        file.close()
        if total>=number and total!=0:
            return True
        else:
            return False
    except:
        return False

main()
    
