def main():
    print('This program calculates exponential values.')
    x=int(input('Enter the base: '))
    y=int(input('Enter the power: '))
    print(x,'^',y,' = ',pwr(x,y),sep='')

def pwr(x,y):
    if y==0:
        return 1
    return pwr(x,y-1)*(x)

main()
