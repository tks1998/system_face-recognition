from django.conf import settings
import os
from . import config
from . import process_Tree
import numpy as np
import heapq
import pickle
from .documents import Information
_dict = {    
    "1":config.origin_HOG_npy,
    "5":config.origin_facenet_npy
}
def process_img(file_name,option):
    """
        get request image 
        Call vp-tree and get similarity image 
    """
    distance = []
    index = []
    infors = []

    filename, file_extension = os.path.splitext(file_name)
   
    
    feature = np.load(os.path.join(settings.MEDIA_ROOT_NPY,filename+".npy"))
   
    if config.VP_buid == False:
        config.VP_buid = True
        config.Tree = process_Tree.vptree(config.VP_range,_dict[option], config.type_distance)
        config.Root = config.Tree.build(0,config.VP_range-1)             
        # path_Tree = os.path.join(settings.BASE_DIR, 'home\\model\\Tree_model_HOG_famous_human.pkl')
        # path_root = os.path.join(settings.BASE_DIR, 'home\\model\\root_model_HOG_famous_human.pkl')
        # loadling1 = open(path_Tree, "rb")
        # loadling2 = open(path_root, "rb")
        # config.Tree = pickle.load(loadling1)
        # config.Root = pickle.load(loadling2)
        # config.Tree.path = config.origin_HOG_npy


    """ reset variable """
    
    config.Tree.heap = []
    config.Tree.current_Ranking = config.Range_find
    """
        test
    """
    

    """ search """
    config.Tree.search(config.Root, feature, config.K_similarity)
    
    while config.Tree.heap:
        x, y = heapq.heappop(config.Tree.heap)
        distance.append(x)
        print(x,y)
        # Nếu up dữ liệu lên thì set 1 = y
        s = Information.search().query("match", name=str(1))
        t = None
        for s1 in s:
            t = s1
            break
        # print("day la ",  t.name, t.description)
        infors.append({
            "img" : str(y)+".png",
            "name" : t.name,
            "description" : t.description
        })
    config.Tree.heap = []
    """ return json include distance and index """
    return {
                "information" : infors,
                "distance"  : distance,
                "origin"    : file_name
            }
            
