def main():
   print('Enter a paragraph. Press enter between each line. Type q on a line by itself to quit.')
   line=input('')
   para=[]
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
       para.append(temp1)
       line=input('')
   wordList=[]
   for index1 in range(len(para)):
       for index2 in range(len(para[index1])):
           if [para[index1][index2]] not in wordList:
               wordList.append([para[index1][index2]])
   wordList.sort()
   for index1 in range(len(wordList)):
       for index2 in range(len(wordList[index1])):
           for pIndex in range(len(para)):
               if wordList[index1][index2] in para[pIndex]:
                   wordList[index1].append(pIndex+1)
   print()
   print('The index for this paragraph is:')
   for index1 in range(len(wordList)):
       for index2 in range(len(wordList[index1])):
           if index2==0:
               print(wordList[index1][index2],':',sep='',end=' ')
           elif index2==(len(wordList[index1])-1):
               print(wordList[index1][index2])
           else:
               print(wordList[index1][index2],end=', ')
main()
