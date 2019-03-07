#!/usr/bin/python3

import math as m

def resolution(pul, pix_ancho, pix_alto):
    hip = m.sqrt(pix_ancho**2 + pix_alto**2)
    anch = int((pul/hip) * pix_ancho * 25.4)
    alto = int((pul/hip) * pix_alto * 25.4)
    return (anch, alto)

N = int(input())
for _ in range(N):
    inp = input().split()
    inp = list(map(float, inp))

    a, b = resolution(inp[0], inp[1], inp[2])
    print(a, b)
