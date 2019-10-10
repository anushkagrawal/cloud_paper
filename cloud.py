# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 14:26:23 2019

@author: ANUSHKA
"""

import numpy as np
import pandas as pd
from array import *
import matplotlib.pyplot as plt 

def fun1(lamda2):
    
    af=0.18*(pow(10,-12))
    bf=cf=0
    
    lamda3=(.5)*lamda2
    lamda1=lamda3
    yw1=((0.6)*lamda1)
    yw2=((1.2)*lamda2)
    yw3=((0.6)*lamda3)

    pwf1=(af*pow(yw1,2))+(bf*yw1)+cf
    pwf2=(af*pow(yw2,2))+(bf*yw2)+cf
    pwf3=(af*pow(yw3,2))+(bf*yw3)+cf
    pwft=pwf1+pwf2+pwf3
    ac=pow(10,-28)
    bc=3
    fc=3
    X=2100
    pc=3.2
    pc1=(X*(.6)*((ac*fc)+bc))/pc
    pc2=(X*(1.2)*((ac*fc)+bc))/pc
    pc3=(X*(.6)*((ac*fc)+bc))/pc
    pc=pc1+pc2+pc3
    
    a1=1
    a2=3
    a3=.1

    pwc=(a1*(0.6)*lamda1)+(a2*(1.2)*lamda2)+(a3*(0.6)*lamda3)
    
    p=pwc+pc+pwft
    return p
    
def fun2(s2):
    
    af=0.18*(pow(10,-12))
    bf=cf=0
    lamda2=20
    lamda3=(.5)*lamda2
    lamda1=lamda3
    yw1=((0.6)*lamda1)
    yw2=((s2)*lamda2)
    yw3=((0.6)*lamda3)

    pwf1=(af*pow(yw1,2))+(bf*yw1)+cf
    pwf2=(af*pow(yw2,2))+(bf*yw2)+cf
    pwf3=(af*pow(yw3,2))+(bf*yw3)+cf
    pwft=pwf1+pwf2+pwf3
    ac=pow(10,-28)
    bc=3
    fc=3
    X=2100
    pc=3.2
    pc1=(X*(.6)*((ac*fc)+bc))/pc
    pc2=(X*(s2)*((ac*fc)+bc))/pc
    pc3=(X*(.6)*((ac*fc)+bc))/pc
    pc=pc1+pc2+pc3
    
    a1=1
    a2=3
    a3=.1

    pwc=(a1*(0.6)*lamda1)+(a2*(s2)*lamda2)+(a3*(0.6)*lamda3)
    
    p=pwc+pc+pwft
    return p

def main():
#    lamda2=[4,6,8,10,12,14,16,18]
     my_array = array('i', [4,6,8,10,12,14,16,18])     
     p=[]   
     j=0
     for i in my_array:
         p.append(fun1(i))
         #print(p[j])
#     for i in range(2):
#        p[i]=power(lamda2[i])
#        print(p[i])
     
     print (p)
     
     plt.plot(my_array,p) 
  
# function to show the plot 
     plt.show()
     
     p2=[]
     s2 = [0.2,0.4,0.6,0.8,1,1.2,1.4,1.6]
     for j in s2:
         p2.append(fun2(j))

     print (p2)        
     p3=[]
     for j in p2:
         p3.append(pow(j,2))
         
     plt.gca().set_color_cycle(['red','green'])
#     plt.plot(s2,p2)
     plt.plot(s2,p3)
     
     
     plt.show()
     
if __name__ == '__main__':
    main()
    