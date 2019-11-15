import os
from . import config
from . import process_Tree
import numpy as np


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
    config.Tree._tau = config.Range_find
    """ search """
    config.Tree.search(config.root, feature, 5)
    for x in config.Tree.heap:
        distance.append(x[0])
        index.append(str(x[1])+".png")
        print(str(x[1])+".png")
        config.Tree.heap = []
    """ return json include distance and index """
    return {"distance": distance,
            "name": index}
