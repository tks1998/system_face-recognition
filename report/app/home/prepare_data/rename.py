import os 
path_img = "C:\\Users\\DELL\\Desktop\\all70k"
new_path_img = "C:\\Users\\DELL\\Desktop\\image_missing"
path_feature = "C:\\Users\\DELL\\Desktop\\new_feature"
new_clean_vector = "C:\\Users\\DELL\\Desktop\clean_vector"
i = 1
for f in os.listdir(path_img):
    name ,extension = f.split('.')
    name_in_npy = "img70k"+name+".npy"
    
    src_img = os.path.join(path_img,f)
    dist_img = os.path.join(new_path_img,str(i)+"."+extension) 
    
    src_npy = os.path.join(path_feature,name_in_npy) #((f.split("k")[1]).split('.')[0]
    dist_npy = os.path.join(new_clean_vector,str(i)+".npy")
    
    if os.path.isfile (src_npy):
        os.rename(src_img,dist_img)
        os.rename(src_npy,dist_npy)
        i = i+1
    if (i%2000):
        print(i)
print("day la tong so",i)