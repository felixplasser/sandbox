#!/usr/bin/env python3

def james(n):
    print('This is James T')
    print('Does this work')


def umatur(n):
    print(n+3)

def dong(n):
    print("Dong here")
    print("Hello")

def felix(n):
    print("This is Felix' code!!")
    print("And it is now even better")
    a = 1
    b = 1
    for i in range(n):
        c = a+b
        print(c)
        a = b
        b = c

def kenny(n):
    print(n**n)

if __name__=='__main__':
    n = 10
    james(n)
    umatur(n)
    dong(n)
    felix(n)
    kenny(n)

