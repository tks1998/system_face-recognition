import os
import numpy as np
import shutil
"""
    make folder prepare split data 
"""
def make_file(origin: int ,part:int,name_folder:str):
    if not os.path.exists(name_folder):
        os.mkdir(name_folder)
    path = os.path.join(os.path.dirname(__file__),name_folder)
    max_folder =  origin//part + 1
    for x in range(1,max_folder+1):
        sub_path = os.path.join(path+"/","part"+str(x))
        if not os.path.exists(sub_path):
            os.mkdir(sub_path)
       
    return True
"""
    path : origin folder data
    example path 
    path = "C:\\Users\\DELL\\Desktop\\train\\"
"""
def get_path_feature(path_origin,number_part,name_folder):
    path = os.path.join(os.path.dirname(__file__),name_folder) # name_folder = "split_data"
    
    for f in os.listdir(path_origin):
        """
            split name && convert suffix -> int && push it in corecct folder 
        """
        number_f = int(f.split('.')[0])
        part = number_f//number_part
        if number_f%number_part !=0:
            part = part + 1
             
        new_path = os.path.join(path,"part"+str(part))
        src = os.path.join(path_origin,f)
        #print(new_path,src)
        shutil.copy(src,new_path)    
    return True

def split(number_part=5,name = ""):
    path_origin_data = "C:\\Users\\DELL\\Desktop\\train"
    number_file_origin = len(next(os.walk(path_origin_data))[2])
    if make_file(number_file_origin,number_part,"split_data") == False:
        return False
    
    get_path_feature(path_origin_data,number_part,name)
    return True
#make_file(20,3,"split_data")
split(1000,"split_data")
