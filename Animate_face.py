import cv2
import sys
import os.path
# import   test  as  teat
import glob
from PIL import Image
import numpy as np
# C:/Users/PC/Pictures/animate_girl/adagio_dazzle_by_raika0306_dcvteiz.png

def detect(cascade_file="C:/Users/PC/Pictures/animate_girl/xml/lbpcascade_animeface.xml"):
    print("!!!!!!")
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)
    #---------------
    Read_path = "F:\Anime_Girl/add_3_filter/"
    Save_path = "F:\Anime_Girl/add_3_filter_CUT/"
    data_path = os.path.join(  Read_path, '*jpg')
    files = glob.glob(data_path)
    print(" data_path -->", data_path)
    count = 27029
    for filename in files:
        # print(" filename  -->",filename )

        #------------- cut
        cascade = cv2.CascadeClassifier(cascade_file)
        image = cv2.imread(filename, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        faces = cascade.detectMultiScale(gray,
                                         # detector options
                                         scaleFactor=1.1,
                                         minNeighbors=5,
                                         minSize=(24, 24))
        # for (x, y, w, h) in faces:
        #     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 0), 2)
        print("faces[0][0]", len(faces))
        if   len(faces) is not 0:
         # print("faces[0][0]", faces)
         a = faces[0][0]-faces[0][0]//3
         print("a",a)
         b = faces[0][1]-faces[0][1]//3
         print("b",b)
         c = faces[0][2]+2*faces[0][2]//3
         print("c",c)
         d = faces[0][3]+2*faces[0][3]//3
         print("d",d)
         check_image=np.array(image)
         if c or d<check_image.shape[0]:
            # image_face_part = image[b:b + d, a:a + c]
            image_face_part = image[faces[0][1]:faces[0][3] + faces[0][1], faces[0][0]:faces[0][2] + faces[0][0]]
            # image_face_part = cv2.resize(image_face_part, (128, 128), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(Save_path+"im("+str(count)+").jpg", image_face_part)
            count=count +1
         else:
             print("hi")
    # return print("done" )




            #-------------

        # ANSWER = IL.filter(filename)
        # if ANSWER == True:
        #     image = cv2.imread(filename, cv2.IMREAD_COLOR)
        #     cv2.imwrite("C:/Users/PC/Pictures/animate_girl/after_filter/" + str(count) + ".jpg", image)
        #     count = count + 1
        # else:
        #     print(" filename  -->", filename)
    #-**-------------





    # print(faces[0])
    # a = faces[0][0]-faces[0][2]//3
    # print(a)
    # b = faces[0][1]-faces[0][3]//3
    # print(b)
    # c = faces[0][2]+2*faces[0][2]//3
    # print(c)
    # d = faces[0][3]+2*faces[0][3]//3
    # print(d)
    # # print((image))
    # # image=np.array(image)
    #
    # image_face_part = image[b:b+d,a:a+c]
    # # print(image_face_part)
    #
    # cv2.imwrite("C:/Users/PC/Pictures/animate_girl/save/test.jpg",image_face_part)
    # cv2.imshow("AnimeFaceDetect", image)
    # cv2.waitKey(0)
    # cv2.imwrite("out.png", image)





# if len(sys.argv) != 2:
#     sys.stderr.write("usage: detect.py <filename>\n")
#     sys.exit(-1)
print("????")

detect()
