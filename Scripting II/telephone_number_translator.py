def letter(x):
    l1=['A','B','C']
    l2=['D','E','F']
    l3=['G','H','I']
    l4=['J','K','L']
    l5=['M','N','O']
    l6=['P','Q','R','S']
    l7=['T','U','V']
    l8=['W','X','Y','Z']
    
    if x==l1[0] or x==l1[1] or x==l1[2]:
        return '2'
    elif x==l2[0] or x==l2[1] or x==l2[2]:
        return '3'
    elif x==l3[0] or x==l3[1] or x==l3[2]:
        return '4'
    elif x==l4[0] or x==l4[1] or x==l4[2]:
        return '5'
    elif x==l5[0] or x==l5[1] or x==l5[2]:
        return '6'
    elif x==l6[0] or x==l6[1] or x==l6[2] or x==l6[3]:
        return '7'
    elif x==l7[0] or x==l7[1] or x==l7[2]:
        return '8'
    elif x==l8[0] or x==l8[1] or x==l8[2] or x==l8[3]:
        return '9'
    else:
        return x
        
def main():
    x=input('Please enter an alphabetic telephone number:')
    tel=''
    for n in x:
        y=letter(n)
        tel=tel+y
    print('The converted telephone number is ',tel,'.',sep='')

main()
