import os
from . import config
from . import process_Tree
import numpy as np
import heapq

def process_img(file_name):
    """
        get request image 
        Call vp-tree and get similarity image 
    """
    q = {}
    distance = []
    index = []
    filename, file_extension = os.path.splitext(file_name)
    feature = np.load(config.path_new_numpy)
    if config.VP_buid == False:
        config.VP_buid = True
        config.Tree = process_Tree.vptree(config.VP_range)
        config.root = config.Tree.build(0, config.VP_range-1)
    """ reset variable """
    config.Tree.heap = []
    config.Tree.current_Ranking = config.Range_find
    """ search """
    config.Tree.search(config.root, feature, config.K_similarity)
    while config.Tree.heap:
        x,y=heapq.heappop(config.Tree.heap)
        distance.append(x)
        index.append(str(y)+".png")
        print(x,y)
    config.Tree.heap = []
    """ return json include distance and index """
    return {"distance": distance,
            "name": index}
