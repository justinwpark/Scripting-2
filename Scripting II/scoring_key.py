key={1:'B',2:'D',3:'A',4:'A',5:'C',6:'A',7:'B',8:'A',9:'C',10:'D',11:'B',12:'C',13:'D',14:'A',15:'D',16:'C',17:'C',18:'B',19:'D',20:'A'}
x=input('Enter a filename: ')
print()
print('Contents of',x)
file=open(x,'r')
count=1
a=0
b=''
c=0
d=''
for line in file:
    line=line.rstrip()
    print(count,': ',line,sep='')
    num=str(count)
    if line in key[count]:
        a+=1
        if b=='':
            b+=num
        else:
            b+=','+num
    else:
        c+=1
        if d=='':
            d+=num
        else:
            d+=','+num
    count+=1



print('Total correctly answered questions:',a)
print('Questions that were answered correctly:',b)
print('Total incorrectly answered questions:',c)
print('Questions that were answered incorrectly:',d)
if a>=15:
    print('This exam receives a passing score.')
else:
    print('This exam receives a failing score.')
