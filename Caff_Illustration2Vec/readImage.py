import numpy as np
import pandas as pd
import cv2
from PIL import Image
import os
import random
import   test  as  teat
import glob
import  Illustration2Vec as IL
from progressbar import *





def read_image():
    progress = ProgressBar()
    #---------------------------------------------------------------
    # Save_path = "F:\Anime_Girl\Anime_save_filter/"
    Read_path = "F:\Anime_Girl/add_3_filter_CUT/"
    Save_path="F:\Anime_Girl/add_3_filter_CUT_filter/"
    data_path = os.path.join(Read_path, '*jpg')
    files = glob.glob(data_path)
    print(" data_path -->", data_path )
    count=29481
    for filename in progress(files):
        # print(" filename  -->",filename )
     try:
        ANSWER=IL.filter(filename )
        if ANSWER==True:
            image = cv2.imread(filename, cv2.IMREAD_COLOR)
            cv2.imwrite(Save_path+"im"+"("+str(count)+")"+".jpg", image)
            count=count+1
        else:
            print(" filename  -->",filename )
     except OSError:
         print(" OSError")
         pass


a=read_image()
# print(a)
# for i in range(0,5):
#  read_image()