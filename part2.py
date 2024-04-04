import numpy as np
#precondition: V is a 1x2 vector, A is an angle in radians
#postcondition: returns V rotated counterclockwise by 'a' radians
def CounterClockRotate(V, A):
    NewX=V[0]*np.cos(A)-V[1]*np.sin(A)
    NewY=V[0]*np.sin(A)+V[1]*np.cos(A)
    return np.array([NewX,NewY])
#precondition: V is a 1x2 vector, A is an angle in radians
#postcondition: returns V rotated clockwise by 'a' radians
def ClockRotate(V, A):
    return CounterClockRotate(V, -A)