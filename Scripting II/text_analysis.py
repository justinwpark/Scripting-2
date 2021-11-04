def count(l1):
    total_of_upper=0
    total_of_lower=0
    total_of_digits=0
    total_of_white=0
    for a in l1:
        for x in a:
            if x.isspace():
                total_of_white+=1
    for a in l1:
        for x in a:
            if x.isupper():
               total_of_upper+=1
    for a in l1:
        for x in a: 
            if x.islower():
                total_of_lower+=1
    for a in l1:
        for x in a:
            if x.isdigit():
                total_of_digits+=1
    print('There are',(total_of_upper),'uppercase letters in this text.')
    print('There are',(total_of_lower),'lowercase letters in this text.')
    print('There are',(total_of_digits),'digits in this text.')
    print('There are',(total_of_white),'whitespace characters in this text.')

def main():
    print('This program analyzes text. Enter text or enter "quit" to quit.')
    x=input('Please enter some text: ')
    l1=[]
    while x!='quit':
        l1.append(x)
        x=input('Please enter some text: ')
    count(l1)

main()
        
