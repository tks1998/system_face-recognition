import numpy as np
import os

def distance(a,b):
    
    a1 = np.load(a) # path
    a2 = np.load(b)
    
    return np.linalg.norm(a1-a2)
if __name__ == '__main__':
    base_dir = "C:\\Users\\DELL\\Desktop\\feature extract VGG"
    a = os.path.join(base_dir,"0.npy")
    b = os.path.join(base_dir,"100.npy")
    print(distance(a,b))
