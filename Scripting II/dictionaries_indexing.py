print('Enter a paragraph. Press enter between each line. Type q on a line by itself to quit.')
line=input('')
index = {}
dict1=index
counter=1
while line!='q':
   line=line.split(' ')
   temp1=[]
   for index in range(len(line)):
       if line[index] == '':
           yep=1
       elif line[index].isalpha():
           temp1.append(line[index].lower())
       elif line[index][-1].isalpha():
           temp1.append(line[index].lower())
       else:
           inc=-1
           while not line[index][ :inc].isalpha():
               inc-=1
           temp1.append(line[index][ :inc].lower())
   for index in temp1:
      count=str(counter)
      if index not in dict1:
         dict1[index]=count
      else:
         if str(counter) not in dict1[index]:
            alpha=dict1[index]
            dict1[index]=(alpha+', '+count)
   counter+=1
   line=input('')
print()
print('The index for this paragraph is:')
keys = []
for key in dict1.keys():
   keys.append(key)
keys.sort()
for index in keys:
    print(index,': ',dict1[index],sep='')
       

