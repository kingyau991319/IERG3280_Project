import numpy as np
import networkx as nx
import main

x = ["Sam","Kanon","Tom","Que"]
size = 8
temp = (size,size)
martix = np.zeros(temp)
martix[1][1]=1
print(martix)
a_del = np.delete(np.delete(martix, 1, 1), 1, 0)
print(a_del)

a = np.arange(12).reshape(3, 4)
print(a)
a_del = np.delete(a, 1, 0)
print(a_del)
