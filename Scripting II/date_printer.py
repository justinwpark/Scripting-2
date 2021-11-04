def convert_month(x):
    l1=['January','February','March','April','May','June','July','August','September','October','November','December']
    if x=='01':
        return l1[0]
    elif x=='02':
        return l1[1]
    elif x=='03':
        return l1[2]
    elif x=='04':
        return l1[3]
    elif x=='05':
        return l1[4]
    elif x=='06':
        return l1[5]
    elif x=='07':
        return l1[6]
    elif x=='08':
        return l1[7]
    elif x=='09':
        return l1[8]
    elif x=='10':
        return l1[9]
    elif x=='11':
        return l1[10]
    else:
        return l1[11]



def main():
    print('This program converts dates.')
    x=input('Please enter a date in the form mm/dd/yyyy: ')
    y=x[0:2]
    month=convert_month(y)
    num=int(x[3:5])
    if num<10:
        print('The converted date is ',(month),' ',x[4:5],', ',x[6:],'.',sep='')
    if num>=10:
        print('The converted date is ',(month),' ',x[3:5],', ',x[6:],'.',sep='')
    

main()
    

    
