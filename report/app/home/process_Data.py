import os
import numpy as np
import pandas as pd
# path = "C:\\Users\\DELL\\Desktop\\system_search\\report\\app\\home\\train"
# all = list([])
# dem = 0
# for x in os.listdir(path):
#     current_file = os.path.join(path,x)
#     a = np.load(current_file)
#     a = np.around(a,4) # resize 4 number after dot
#     all.append(a)
#     if dem==2:
#         break
#     dem = dem +1

# print(all)
# np.savetxt('data.txt',all, delimiter = ',')

    

base_path = os.path.join(os.path.dirname(__file__),"data.txt")

with open(base_path) as fp:
    for line in fp:
        print(type(line))   
        break
# text_file = open("data.txt", "r")
# lines = text_file.readlines()
# pre_data = lines[0].split(',')
# x = float(pre_data[-1].split('\n')[0])
# print(round(x,4))
# text_file.close()