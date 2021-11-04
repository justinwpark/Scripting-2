def main():
    print('This program keeps a running total of your shopping list.')
    print("Use 'EXIT' to exit.")
    file=open('shopping.txt','r')
    l1={}
    file.readline()
    for line in file:
        l1[line.rstrip().lower()]=float(file.readline().rstrip())
    x=input('Enter an item: ')
    total=0
    while x!='EXIT':
        try:
            total+=l1[x.lower()]
            print('Your current total is $',format(total,'.2f'),sep='')
            print()
        except KeyError:
            print('That is not a valid item.')
            print()
        x=input('Enter an item: ')
    print('Your final total is $',format(total,'.2f'),sep='')

main()
