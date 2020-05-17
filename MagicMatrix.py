## -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 22:58:00 2019

@author: simon880502
"""
import time

def Line():
        print('='*35)
def Magic():
    global t0,t1,useTime
    i=0
    j=(N-1)//2
    sq[i][j]=1
    key=2
    #============
    while key<=N*N:
        p=i-1
        q=j-1
        if sq[p][q] !=0:
          p=i+1
          q=j
        if p<0 and q<0:
          p=i-1
          q=j
        if p<0:
          p+=N
        if q<0:
            q+=N
        sq[p][q]=key
        i=p
        j=q
        key+=1

        
def show():
    global useTime
    for i in range(N):    
        for j in range(N):
            print('%5d'%sq[i][j],end='')
        print('\n')
    Line()
    print('The sum of any row (column,diagonal) is',sum(sq[i][j] for i in range(N)),end='\n')
    Line()
def check():
    x=sum(sq[i][0] for i in range(N))
#    row check
    Line()
    for i in range(N):
        if x==sum(sq[i][j] for j in range(N)):
            print('Row ',i+1,'checked✓')
            time.sleep(.1)
    Line()
    for i in range(N):
        if x==sum(sq[j][i] for j in range(N)):
            print('Column ',i+1,'checked✓')
            time.sleep(.1)
    Line()
    if x==sum(sq[j][j] for j in range(N)):
        print('Diagonal 1 checked✓')
    if x==sum(sq[N-1][N-1-j] for j in range(N)):
        print('Diagonal 2 checked✓')
        
while True:
  N=int((input('Enter an odd number(less than 16) to be the size of magic matrix  :')))
  s=str(N)
  if N%2==0 or N<=2 or N>=16 or s.isdigit()==False:
    print('ERROR')
  else:
    break
sq=[[0]*N for row in range(N)]
Magic()
print('\n')
show()
input("!!! Press Enter to go Checking Mode !!!")
check()
