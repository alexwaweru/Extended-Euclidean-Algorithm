'''@author: Alex Waweru'''
def gcd(a,b):
    q,x,y,xl,yl = 0,0,1,1,0; temp = _extended_euclidean(a,b,x,y,xl,yl)
    return "gcd = "+str(temp[0])+", x="+str(temp[1])+" y="+str(temp[2])

def _extended_euclidean(a,b,x,y,xl,yl):
    while b!=0:
        q = a//b; a,b = (b, a%b); x,xl = (xl-q*x,x); y,yl = (yl-q*y,y)
    return a,xl,yl


