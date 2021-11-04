def main():
    print("Please enter some numbers. Type 'q' to quit.")
    x=input('Enter a number: ')
    l1=[]
    a=0
    while x!='q':
        x=int(x)
        l1.append(x)
        x=input('Enter a number: ')
    print('The lowest number is',min(l1))
    print('The highest number is',max(l1))
    b=len(l1)
    for n in l1:
        a=a+n
    print('The total of the numbers is',a)
    print('The average of the numbers is',format(a/b,'.2f'))
        

main()
    
        
        
    
