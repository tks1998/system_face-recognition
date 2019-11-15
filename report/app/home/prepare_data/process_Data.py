import os
import shutil 
new_path  ="C:\\Users\\DELL\\Desktop\\new_feature"
path_origin_data = "C:\\Users\\DELL\\Desktop\\feature"
for f in os.listdir(path_origin_data):
    shutil.copy(os.path.join(path_origin_data,f),new_path)
    
# new_path = "C:\\Users\\DELL\\Desktop\\all70k"
# path_origin_data = "C:\\Users\\DELL\\Desktop\\img70k"
# for f in os.listdir(path_origin_data):
#     new_f = os.path.join(path_origin_data,f)
#     for file_ in os.listdir(new_f):
#         shutil.copy(os.path.join(new_f,file_),new_path)