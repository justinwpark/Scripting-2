def main():
    print('This program calculates the greatest common divisor (GCD) for two integers.')
    print()
    a=int(input('Enter a number: '))
    b=int(input('Enter another: '))
    print()
    print('GCD =',gcd(a,b))

def gcd(m,n):
    if n==0:
       return m
    if n!=0:
        return gcd(n, m%n)


main()
