months=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
positions=['1st', '2nd', '3rd', '4th']

def main():
    print('This program divides a group of people into jury pools.')
    file_name=input('Enter a file name: ')
    number_of_months=verify_mwj('Enter the number of months: ',12)
    number_of_weeks=verify_mwj('Enter the number of weeks: ',4)
    jur=480//(number_of_months*number_of_weeks)
    number_of_jurors=verify_mwj('Enter the number of people in each jury pool: ',jur)

    a=verify_file(file_name,number_of_jurors)
    if a==False:
        print('There was a problem with the file:',file_name)
    if a:
        jurypools=[]
        file_x=open(file_name, 'r')
        for index1 in range(number_of_months):
            temp1=[]
            for index2 in range(number_of_weeks):
                temp2=[]
                for index3 in range(number_of_jurors):
                    temp2.append(file_x.readline().rstrip())
                temp1.append(temp2)
            jurypools.append(temp1)
        file_x.close()
        print('')
        print('Enter a month, week, and juror number to select a juror.')
        y='y'
        while y=='y' or y=='Y':
            month=verify_mwj('Select a month: ',number_of_months)
            weeks=verify_mwj('Select a week: ',number_of_weeks)
            juror=verify_mwj('Select a juror number: ',number_of_jurors)
            print('Juror #',juror,' for the ',positions[weeks-1],' week of ',months[month-1],' is ',jurypools[month-1][weeks-1][juror-1],'.',sep='')

            print('')
            y=input('Would you like to find another juror? (y/n) ')
            while y!='n' and y!='N' and y!='y' and y!='Y':
                print('Invalid input.')
                print('')
                y=input('Would you like to find another juror? (y/n) ')
                
                
                    
def verify_file(filename,number):
    try:
        total=0
        file=open(filename,'r')
        for line in file:
            line=line.rstrip()
            total+=1
        file.close()
        if total>=number and total!=0:
            return True
        else:
            return False
    except:
        return False

def verify_mwj(message,maximum):
    valid=input(message)
    a=1
    while a==1:
        try:
            valid=int(valid)
            while valid<=0 or valid>maximum:
                print('You must enter a number in the range [1, ',maximum,'].',sep='')
                valid=int(input(message))
            a=0
        except:
            print('You must enter an integer value.')
            valid=input(message)
    return valid






main()
    



    
