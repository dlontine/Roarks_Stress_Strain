# -*- coding: utf-8 -*-
"""
This script develops methods for some of the base coefficients in Reddy_Ch11
"""
###-----Required Definitions-----##
v=.3    #Poisson's Ratio
a=10    #Typically outside diameter
b=5     #Typically inside diameter of annular plate
r=6     #Typically the radius of interest
ro=7    #Radius at which action is starting/ending

################################
####------ F Functions -----####
################################

F1=(1+v*a)/2*b/r*log(r/b)+(1-v)/4*(r/b-b/r)
F2=1/4*(1-(b/r)**2*(1+2*log(r/b)))
F3=b/(4*r)*(((b/r)**2+1)*log(r/b)+(b/r)**2-1)
F4=1/2*((1+v)*(b/r)+(1-v)*r/b)
F5=1/2*(1-(b/r)**2)
F6=b/(4*r)*((b/r)**2-1+2*log(r/b))
F7=1/2*(1-v**2)*(r/b-b/r)
F8=1/2*(1+v+(1-v)*(b/r)**2)
F9=b/r*/((1+v)/2*log(r/b)+(1-v)/4*(1-(b/r)**2))
F=array([F1,F2,F3,F4,F5,F6,F7,F8,F9])

################################
####------ C Functions -----####
################################
C1=(1+v)/2*(b/a)*log(a/b)+(1+v)/4*(a/b-b/a)
C2=1/4*(1-(b/a)**2*(1+*log(a/b)))
C3=b/(4*a)*(((b/a)**2+1)*log(a/b)+(b/a)**2-1)
C4=1/2*((1+v)*b/a+(1-v)*a/b)
C5=1/2*(1-(b/a)**2)
C6=b/(4*a)*((b/a)**2-1+2*log(a/b))
C7=1/2*(1-v**2)*(a/b-b/a)
C8=1/2*(1+v+(1-v)*(b/a)**2)
C9=b/a*((1+v)/2*log(a/b)+(1+v)/4*(1-(b/a)**2))
C=array([0,C1,C2,C3,C4,C5,C6,C7,C8,C9])

################################
####------ L Functions -----####
################################
L1=(1+v)/2*ro/a
L2=1/4*(1-(ro/a)**2*(1+2*log(a/ro)))
L3=ro/(4*a)*(((ro/a)**2+1)*log(a/ro)+(ro/a)**2-1)
L4=1/2*((1+v)*ro/a+(1-v)*a/ro)
L5=1/2*(1-(ro/a)**2)
L6=ro/(4*a)*((ro/a)**2-1+2*log(a/ro))
L7=1/2*(1-v**2)*(a/ro-ro/a)
L8=ro/a*(1+v+(1-v)*(ro/a)**2)
L9=ro/a*((1+v)/2*log(a/ro)+(1-v)/4*(1-(ro/a)**2))
L11=1/64*(1+4*(ro/a)**2-5*(ro/a)**4-4*(ro/a)**2*(2+(ro/a)**2)*log(a/ro))
L12=a/(14400*(a-ro))*(64-225*ro/a-100*(ro/a)**3+261*(ro/a)**5+60*(ro/a)**3*(3*(ro/a)**2+10)log(a/ro))
L13=25-128*ro/a+225*(ro/a)**2-25*(ro/a)**4-97*(ro/a)**6-60*(ro/a)**4*(5+(ro/a)**2)*log(a/ro)
L13*=a**2/(14400*(a-ro)**2)
L14=1/16*(1-(ro/a)**4-4*(ro/a)**2*log(a/ro))
L15=a/(720*(a-ro))*(16-45*ro/a+9*(ro/a)**5+20*(ro/a)**3*(1+3*log(a/ro)))
L16=a**2/(1440*(a-ro)**2)*(15-64*ro/a+90*(ro/a)**2-6*(ro/a)**6-5*(ro/a)**4*(7+12*log(a/ro)))
L17=1/4*(1-(1-v)/4*(1-(ro/a)**4)-(ro/a)**2*(1+(1+v)*log(a/ro)))
L18=(20*(ro/a)**3+16)*(4+v)-45*ro/a*(3+v)-9*(ro/a)**5*(1-v)+60*(ro/a)**3*(1+v)*log(a/ro)
L18*=a/(720*(a-ro))
L19=15*(5+v)-64*ro/a*(4+v)+90*(ro/a)**2*(3+v)-5*(ro/a)**4*(19+7*v)
L19+=6*(ro/a)**6*(1-v)-60*(ro/a)**4*(1+v)*log(a/ro)
L19*=a**2/(1440*(a-ro)**2)
L=array([0,L1,L2,L3,L4,L5,L6,L7,L8,L9,0,L11,L12,L13,L14,L15,L16,L17,L18,L19])

################################
####------ G Functions -----####
################################
