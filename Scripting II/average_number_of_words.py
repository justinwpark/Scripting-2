def amount(l1):
    a=0
    for x in l1:
        y=x.split()
        a+=len(y) 
    return a

        
def main():
    print('Please enter some sentences. Type "quit" on a line by itself to quit.')
    l1=[]
    a=0
    x=input('')
    while x!='quit':
        l1.append(x)
        x=input('')
        a+=1
    y=amount(l1)
    print('These sentences have an average of',format(y/a,'.2f'),'words.')
        
    
main()
    
