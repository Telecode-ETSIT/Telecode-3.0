#!/usr/bin/python3

def play(n):
    while n > 0:
        n = n >> 1
        m = int(input())
        if m != n:
            return False
    return True

N = int(input())
for _ in range(N):
    n = int(input())
    if play(n):
        print("GANADORES")
    else:
        print("DESCALIFICADOS")
        n = int(input())
        while n != 0:
            n = int(input())
        
