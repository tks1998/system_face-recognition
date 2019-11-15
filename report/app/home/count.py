import os

origin_path = "C:\\Users\\DELL\\Desktop\\img70k"

dem  = 0 
for f in os.listdir(origin_path):
    new_ = os.path.join(origin_path,f)
    for k in os.listdir(new_):
        dem=dem+1
print(dem)