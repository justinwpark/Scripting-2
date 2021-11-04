def main():
    print('This program calculates numbers in the Fibonacci sequence.')
    n=int(input('Which place in the sequence do you want to calculate? '))
    print('Fibonacci(',n,') is ',fib(n),sep='')

def fib(n):
    if n<2:
        return n
    return fib(n-2)+fib(n-1)

main()
