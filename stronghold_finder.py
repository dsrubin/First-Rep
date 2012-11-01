import math
###########
# Input
###########
#coordinates of first toss
x1=218.86018
y1=250.40568
#angle in which the first eye moves
deg1=-61.800903

#coordinates of second toss
x3=751.388
y3=536.5642
#angle in which the second eye moves
deg2=153.7485
###############

#convert angle to randians
rad1=math.radians(deg1)
#find second point for line 1
x2=x1-math.sin(rad1)
y2=y1+math.cos(rad1)

#convert angle 2 to radians
rad2=math.radians(deg2)
#find second point for line 2
x4=x3-math.sin(rad2)
y4=y3+math.cos(rad2)


m1=(y2-y1)/(x2-x1) #find slope 1
b1=y1-m1*x1 #find y-intercept 1
m2=(y4-y3)/(x4-x3) #find slope 2
b2=y3-m2*x3 #find y-intercept 2

#solve system of equations for x,y
xf=(b1-b2)/(m2-m1) 
yf=m1*xf+b1

print "Location of stronghold: (",xf,",",yf,")"