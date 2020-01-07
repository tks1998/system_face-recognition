from django.conf import settings
import os
from . import config
from . import process_Tree
import numpy as np
import heapq
import pickle
from .documents import IR2
_dict = {    
    "1":config.origin_HOG_npy,
    "2":config.origin_sift_npy,
    "3":config.origin_mix_hog_sift,
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

    config.Tree = process_Tree.vptree(config.VP_range,_dict[option], config.type_distance)
    config.Root = config.Tree.build(0,config.VP_range-1)             
   
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

        s = IR2.search().query("match", iddata=str(y))
        t = None
        for s1 in s:
            t = s1
            break
        if t is not None:
            print("day la ",  t.name, t.description)
            infors.append({
                "img" : str(y)+".png",
                "name" : t.name,
                "description" : t.description
            })
        else:
            infors.append({
                "img" : str(y)+".png",
                "name" : y,
                "description" : "cannot init name "
            })
    config.Tree.heap = []
    """ return json include distance and index """
    
    return {
                "information" : infors,
                "distance"  : distance,
                "origin"    : file_name
            }
            
