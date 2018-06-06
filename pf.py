# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 01:17:21 2018

# a Python Package for Assessing the Pfaffian (PPAP ≠ Pen Pineapple Apple Pen)
# Calculate the Pfaffian of skew-symmetric matrix (even order)
# potential issue:  the second last line in iter(X), I can't explain it.
# 计算一个反对称偶数阶矩阵的法夫式(Pfaffian)
# 可能存在的问题：iter(X) 函数里面 a=a*(1-2*np.remainder(i+j-1,2)) 说不清楚

@author: Jian Wang
@github: https://github.com/Jian2017/
"""

import numpy as np

def pf(X):
    
    Ni=X.shape[0]
    Nj=X.shape[1]
    
    if np.remainder(Ni,2)!=0:
        print("odd dimensional matrix!")
        assert(0)
        return 0
    
    if abs(X.transpose()+X).max()!=0:
        print("matrix is not skew-symmetric!")
        assert(0)
        return 666
    
    if Ni!=Nj:
        print("matrix is not a square matrix")
        assert(0)
        return 888
        
    
    output=1
    
    while Ni>0:
        a,XX=iter(X)
        X=XX
        Ni=Ni-2
        output=output*a
    
    return output

def iter(X):
    a,i,j=largest(X)
    B,C=getBC(X,i,j)
    
    invA=np.zeros((2 ,2), dtype=complex)
    invA[1,0]=1/a
    invA[0,1]=-invA[1,0]

    XX=C+np.matmul(np.matmul(B.transpose(),invA),B)
    
    a=a*(1-2*np.remainder(i+j-1,2))    # 可能存在的问题
    return a,XX

def largest(X):
    Xabs=abs(X)
    a_temp=Xabs[0,1]
    i_temp=0
    j_temp=1
    for i in range(X.shape[0]):
        for j in range(i,X.shape[1]):
            if Xabs[i,j]>a_temp:
                a_temp=Xabs[i,j]
                i_temp=i
                j_temp=j
    return X[i_temp,j_temp],i_temp,j_temp

def getBC(X,i,j):
    if i>j:
        print("error in getBC!")
        assert(0)
        
    Nx=X.shape[0]
        
    ij=list([i,j])
    idx=list(range(0,i))+list(range(i+1,j))+list(range(j+1,Nx))
        
    C=X[idx,:][:,idx]
    B=X[ij,:][:,idx]
    
    return B,C
