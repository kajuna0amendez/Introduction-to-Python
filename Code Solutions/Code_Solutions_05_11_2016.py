# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 17:40:23 2016

@author: Andres

Solutions for the homework

"""


def Geometric_Series(N,r):
    
    """
    A simple implementation of the Geometric Series.
    
    It accumulates the product
    
    INUPUT
        1.- N Largest power in the Geometric Series
        2.- The Base for the Geometric Series
    OUTPUT
        1.- the final result of the Geimetric Series
    """
    t  = 1
    SN = 0;
    
    for i in range(N+1):
        SN = t
        t  = r*t
        
    return SN
    
def Rec_Fibonacci(N):
    RecFib = lambda x: 0 if x==0 else 1 if x==1 else RecFib(x-1) + RecFib(x-2) 
    return RecFib(N)

def Rec_Factorial(N):
    RecFact = lambda x: "Error" if x<0 else 1 if x==0 else x*RecFact(x-1)
    return RecFact(N)

def Iter_Fibonacci(N):
    Fib1 = [0]
    Fib1 = Fib1 + [1]
    
    n = 1
    while n<N:
        temp = Fib1[-1]+Fib1[-2]
        Fib1[-2] = Fib1[-1]
        Fib1[-1] = temp
        n+=1
        
    return Fib1[-1]
    
def Poly(a,r):
    
    N = len(a)
    p = range(N)
    t = lambda  a,x : a*r**x
    
    return sum (map(t,a,p))
    
def Mat_Mult(A,B,N):
    """
    INPUT
        Flatten Matrices
    OUTPUT 
        Flatten Matrix C = AB
    """
    
    mul = lambda x,y : x*y

    C = []
        
    for i in range(N):
        Ar = A[i*N:i*N+N]
        for j in range(N):
            Br = [B[x] for x in range(len(B)) if x%N==j ]
            #print Ar,Br
            C = C+[sum(map(mul,Ar,Br))]
    return C
    
def Metric_Distance(x,y, select):
     
    Distance1 = { 'Euclidean': lambda x,y: (x - y)**2,
                  'Manhattan' : lambda x,y: abs(x-y)
                }
                
    Distance2 = { 'Euclidean': lambda x: sum(x)**0.5,
                  'Manhattan' : lambda x: sum(x)
                }

    return Distance2[select](map(Distance1[select],x,y))
                       
        
if __name__ == "__main__":
    
    #print Rec_Fibonacci(3)
    
    #print Iter_Fibonacci(3)
    
    #print Poly( [1]*3 , 2)

    N = 3

    A = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    B = [1, 0, 0, 0, 1, 0, 0, 0, 1]

    #print Mat_Mult(A,B,N)    
    
    # print Rec_Factorial(3)
    
    x = [1,1,1]
    y = [0,0,1]
    
    print Metric_Distance(x,y,'Euclidean')