#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 20:26:56 2019

@author: sai
"""
import numpy as np
import random

#x = [[20, 25, 12, 45], [30, 28, 13, 56], [23, 24, 14, 46], [23, 25, 15, 60], [25, 25, 16, 55], [25, 28, 17, 59]]

n = int(input("enter the number of the subjects :- "))
X = [[] for _ in range(n)]
for s in range(n):
    f = int(input("enter No of sub ject take in to the counting:-"))
    if f <= 4:
        for c in range(f):
            if c == 0:
                Mark = int(input("Enter best marks in all CA1 for 30 :-"))
                Mark2 = int(input("Enter best marks in all CA2 for 30:-"))
                if Mark <= 30 and Mark2 <= 30:
                    avg = (Mark+ Mark2) / 60
                    avg = avg * 25
                    X[s].append(avg)
                else:
                    print("sorry")
                    X[s].append(0)
            if c == 1:
                Mark = int(input("Enter best marks in all MID for 40 :-"))
                if Mark <= 40:
                    avg = Mark / 40
                    avg = avg * 20
                    X[s].append(avg)
                else:
                    X[s].append(0)
            if c == 2:
                Mark = int(input("Enter best marks in all END for 75 :-"))
                if Mark <= 75:
                    avg = Mark / 75
                    avg = avg*50
                    X[s].append(avg)
                else:
                    X[s].append(0)
            if c == 3:
                Mark = int(input("Enter attendence :-"))
                if Mark >= 90 and Mark <= 100:
                    X[s].append(5)
                elif Mark >= 85:
                    X[s].append(4)
                elif Mark >= 80:
                    X[s].append(3)    
                elif Mark >= 75:
                    X[s].append(2)
                else:
                    X[s].append(0)
    else:
        print("sorry sir you have entered more subjects")
        for i in range(f):
            X[s].append(0)
                  
w = []
for i in range(f):
    w.append(1)

t = []
b = 0.5

out = []
act = []
for i in range(len(X)):
    k = 0
    for j in range(len(w)):
        k = k + X[i][j] * w [j]
    k = k + b
    if k >= 40:
        act.append("PASS")
    else:
        act.append("FAIL")
    out.append(k)
    
grade = []
for k in range(len(out)):
    if out[k] < 40:
        grade.append('E')
    elif out[k] >=40 and out[k] <= 45:
        grade.append('C')
    elif out[k] >=46 and out[k] <= 55:
        grade.append('B')
    elif out[k] >=56 and out[k] <= 65:
        grade.append('B+')
    elif out[k] >=66 and out[k] <= 75:
        grade.append('A')
    elif out[k] >=76 and out[k] <= 80:
        grade.append('A+')
    else:
        grade.append('O')