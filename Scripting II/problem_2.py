def main():
    print('This program uses a two dimensional list.')
    print('Please enter the numbers in your list. To quit type "quit".')
    x=input('')
    list1=[]
    while x!="quit":
        x=[int(x)]
        list1.append(x)
        x=input('')
    a=int(input('Please enter the value by which you wish to increment: '))
    print('')
    inc_list(a,list1)

def inc_list(a,list1):
    for index1 in range(len(list1)):
        for index2 in range(len(list1)-1):
            list1[index1].append(list1[index1][index2]+a)
    for index1 in range(len(list1)):
        for index2 in range(len(list1[index1])):
            if index2==len(list1[index1])-1:
                print(list1[index1][index2])
            else:
                print(list1[index1][index2],end=' ')
            

main()
        
