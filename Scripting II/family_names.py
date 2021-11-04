print('This program determines which family is the largest, the smallest, and greets each of them.')
file=open('names.txt','r')
family={}
for key in file:
    family[key.rstrip()]=file.readline().rstrip().split(',')
for a in family:
    x=a
    y=a
for a in family:
    if len(family[a])>len(family[x]):
        x=a
    if len(family[a])<len(family[y]):
        y=a
print()
print('The',x,'family is the largest.')
print('The',y,'family is the smallest.')
print()

l1=[]
for a in family:
    l1.append(a)
l1.sort()

for a in l1:
    l2=[]
    for b in range((len(family[a]))-1):
        if b>1:
            d=family[a][b]
            l2.append(d)

    line=''
    if family[a][1]=='':
        line+='Hello, Mr. '
        line+=a
    elif family[a][0]=='':
        line+='Hello, Mrs. '
        line+=a
    else:
        line+='Hello, Mr. and Mrs. '
        line+=a

    if len(l2)!=0:
        for c in l2:
            line+=', '
            line+=c

    l3=[]
    for e in range(len(family[a])):
        if e>1:
            f=family[a][e]
            l3.append(e)

    if len(l3)>0:
        line+=', and '
        line+=family[a][((len(l3))+1)]
    

    
    line+='.'
    
    print(line)
    
    
        

