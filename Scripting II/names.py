def main():
    print('Enter some first names. Enter "quit" to quit.')
    f=[]
    x=0
    first=input('')
    while first!='quit':
        f.append(first)
        first=input('')
        x+=1
    f.sort()
    print('Enter some middle names. Enter "quit" to quit.')
    m=[]
    middle=input('')
    while middle!='quit':
        m.append(middle)
        middle=input('')
    m.sort()
    print('Enter some last names. Enter "quit" to quit.')
    l=[]
    last=input('')
    while last!='quit':
        l.append(last)
        last=input('')
    l.sort()
    alphabatize(f,m,l)


def alphabatize(f,m,l):
    print('')
    print('Full name\t\tInitials')
    print('--------------------------------')
    if len(f)<=len(m) and len(f)<=len(l):
        shortest=len(f)
    elif len(m)<=len(l):
        shortest=len(m)
    else:
        shortest=len(l)
        
    for x in range(shortest):
        print(f[x],' ',m[x],' ',l[x],'\t',f[x][0].upper(),m[x][0].upper(),l[x][0].upper(),sep='')

    for x in range(shortest,len(f)):
        if x==shortest:
            print('')
            print('Leftover first names:')
        print(f[x])
    for x in range(shortest,len(m)):
        if x==shortest:
            print('')
            print('Leftover middle names:')
        print(m[x])
    for x in range(shortest,len(l)):
        if x==shortest:
            print('')
            print('Leftover last names:') 
        print(l[x])
        
        

main()

