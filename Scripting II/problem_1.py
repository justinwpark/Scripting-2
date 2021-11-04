def listprinter(tictactoe): 
   if type(tictactoe).__name__ != 'list': 
       print('You should be using a list!') 
       return False 
   for element in tictactoe: 
       if type(element).__name__ != 'list': 
           print('You should be using a list!') 
           return False 
       for character in element: 
           print(character,end=" ") 
       print()

def main():
    print('This program formats tic-tac-toe boards.')
    x=input('Enter the board: ')
    l1=[]
    l2=[]
    l3=[]
    l4=[]
    l5=[]
    for a in x:
        l2.append(a)
    l3=l2[0:3]   
    l4=l2[3:6]
    l5=l2[6:9]
    l1=[l3,l4,l5]
    listprinter(l1)

main()
