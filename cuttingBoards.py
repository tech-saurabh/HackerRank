# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 14:23:17 2019

@author: Saurabh
"""



def minimumcost(ycost,xcost,yseg,xseg,costsum):
    for i in range( len(xcost) + len(ycost) ):
        if(len(xcost) and len(ycost) == True):
        if(max(ycost)>=max(xcost) and xseg<=yseg):
            a=max(ycost)
            costsum=costsum +(a*xseg)
            print(a,'*',xseg,'->',costsum)
            yseg+=1
            ycost.remove(a)
    
        elif(max(xcost)>=max(ycost) and yseg<=xseg):
            b=max(xcost)
            costsum=costsum+(b*yseg)
            print(b,'*',yseg,'->',costsum)
            xseg+=1
            xcost.remove(b)

        else:
            if(len(ycost)>=len(xcost)):
                if(max(ycost)>=max(xcost) and xseg>=yseg):    
                    c=max(ycost)
                    costsum=costsum +(c*xseg)
                    print(c,'*',xseg,'->',costsum)
                    yseg+=1
                    ycost.remove(c)
                    
                else:
                    d=max(xcost)
                    costsum=costsum +(d*yseg)
                    print(d,'*',yseg,'->',costsum)
                    xseg+=1
                    xcost.remove(d)
            else:
                if(len(xcost) or len(ycost) == 0):
                    if(len(ycost)>0):
                        
                        
                

    return costsum   
           
if __name__ == '__main__':    
    costsum=0
    ycost=[2,1,3,1,4]
    xcost=[4,1,2]
    yseg=1
    xseg=1
    result=minimumcost(ycost,xcost,yseg,xseg,costsum)
    print(result)        