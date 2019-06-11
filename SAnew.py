import random;
import math;
from random import randrange, uniform;
from math import *;


def AP(sol, old, T1) :
    ap = e**(-1*(sol-old))/(T1*1.0);
    return ap;

def rdm():
    x = random.uniform (-10, 10);
    return x;

def fun(x,y):
    F = -abs(math.sin(x)*(math.cos(y))*(exp(abs(1-(math.sqrt(x**2 + y**2)/pi)))));
    return F;

def main():
    
    T1 = 1000;
    A = 0.9;
    T2 = 1;
    x = rdm();
    y = rdm();
    old = fun(x, y);
    while (T1 > T2) :
        LIMIT=100;
        while(LIMIT != 0) :
            x1 = rdm();
            y1 = rdm();
            sol = fun(x1, y1);
            if(sol < old):
                x = x1;
                y = y1;
                old = sol;
            if (AP(sol, old, T1) > random.random ()):
                x = x1;
                y = y1;
                old = sol;
            LIMIT = LIMIT - 1;
        T1 = A * T1;

    print('x1 : ',x)
    print('x2 : ',y)
    print ('solusi minimum : ',old);
    print(fun(8.05502, 9.66459));
    print (math.sin(radians(10)));

    a = input()

main();

           
