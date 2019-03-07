#!/usr/bin/python3

a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

def cesar_cipher(m, k):
    o = ""
    for c in m:
        i = (a.index(c) + k) % len(a)
        o += a[i]
    return o

def probable_words(m):
    ws = ["CESAR", "LEGIONES", "GALIA", "VERCINGETORIX", "GERGOVIA", "FRENTE"]
    for w in ws:
        if w in m:
            return True
    return False

n = int(input())
for _ in range(n):
    m = input()
    for k in range(len(a)):
        o = cesar_cipher(m, k)
        if probable_words(o):
            print(o)
            break
