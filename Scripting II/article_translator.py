print('This program translates articles into more legible English.')
x=input('Enter the "best" word and its list of synonyms. Type "quit" to end input.\n')
word={}
while x!='quit':
    l1=x.split()
    l2=l1[1:]
    word[l1[0]]=l2
    x=input('')
print()
y=input('Enter the article one line at a time. Type "quit" to end input.\n')
article=[]
while y!='quit':
    templ=y.split()
    article.append(templ)
    y=input('')

print() 
print('The modified article is as follows:')
for index in article:
    for index1 in range(len(index)):
        replace=True
        for index2 in word.keys():
            if index[index1] in word[index2]:
                print(index2, end='')
                replace=False
        if replace:
            print(index[index1], end='')
        if index1<len(index)-1:
            print(' ',end='')
    print()

            
           
            
