#-*- coding: utf-8 -*-
import numpy as np

#行数の記入
horizen = 10
#列数の記入
vertical = 8

all_list = []
i=0
for i in range(vertical):
    j=0
    horizen_list = []
    for j in range(horizen):
        horizen_list.append(0)
    all_list.append(horizen_list)
    i+= 1
print(np.array(all_list))