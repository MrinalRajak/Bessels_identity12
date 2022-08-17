
#Bessel's identity
#(12)

import numpy as np
from scipy.special import jn
from scipy.integrate import quad
from scipy.misc import derivative

n=1
x=float(input("Enter the x: "))
theta=int(input("Enter the theta: "))
LHS=np.sin(x*np.cos(theta))
term=2*(-1)**(n+1)*jn(2*n-1,x)*np.cos((2*n-1)*theta)
RHS=term
s=0.0
while(abs(LHS-RHS)>1.0e-5):
    term=2*(-1)**(n+1)*jn(2*n-1,x)*np.cos((2*n-1)*theta)
    s=s+term
    RHS=s
    n=n+1

print("LHS: ",LHS)
print("RHS: ",RHS)
