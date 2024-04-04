import numpy as np
#precondition: V is a 1x2 vector, A is an angle in radians
#postcondition: returns V rotated counterclockwise by 'a' radians
def CounterClockRotate(V, a):
    newX=V[0]*np.cos(a)-V[1]*np.sin(a)
    newY=V[0]*np.sin(a)+V[1]*np.cos(a)
    return [newX,newY]
#precondition: V is a 1x2 vector, A is an angle in radians
#postcondition: returns V rotated clockwise by 'a' radians
def ClockRotate(V, a):
    return CounterClockRotate(V, -a)
#returns V rotated over the X-axis
#precondition: V is a 1x2 vector
def ReflectX(V):
    V[1]=-V[1]
    return V
#returns V over the Y-axis
#precondition: V is a 1x2 vector
def ReflectY(V):
    V[0]=-V[0]
    return V
#returns V flipped over the line Y=X
#precondition: V is a 1x2 vector
def ReflectYX(V):
    return [V[1],V[0]]
#reflects V over Y=mX using matrix 1/(m^2+1)* [1-m^2   2m]
#precondition: V is 1x2 matrix, m is scalar   [2m   m^2-1]
def ReflectYMX(V, m):
    k=m*m+1
    newX=((1-m*m)*V[0]+2*m*V[1])/k
    newY=(2*m*V[0]+(m*m-1)*V[1])/k
    return [newX, newY]

