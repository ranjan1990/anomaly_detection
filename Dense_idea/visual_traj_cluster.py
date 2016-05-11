import cv2
import numpy as np
#image show with normal window
def imshow1(frame):
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow("image",frame);
    cv2.waitKey(10)
               
               
#image show uning matplot
def imshow(img):
    from matplotlib import pyplot as plt
    plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()





#line=(x,y,frame_number)
def draw_circle(src_path,dest_path,line):
    frame_num=int(float(line[2]))+1 #+1 because frame number statrs from 0

    x=int(float(line[0]))
    y=int(float(line[1]))

    if(frame_num<10):
        f_name="x_00"+str(frame_num)+".ppm"
    elif(frame_num<100):
        f_name="x_0"+str(frame_num)+".ppm"
    elif(frame_num<1000):
        f_name="x_"+str(frame_num)+".ppm"
    p=src_path+f_name
    img=cv2.imread(p);
    cv2.circle(img,(x,y),3, (0,0,255), -1)
    imshow1(img)





src_path="/home/ranjan/Kaggle/dense_tracker_ECCV10/moseg/data/UCSD_Anomaly/UCSDped1/Test/Test001/"
dest_path="/home/ranjan/Kaggle/dense_tracker_ECCV10/moseg/data/UCSD_Anomaly/UCSDped1/Test/Test001/"
traj_file="Test001_cluster_traj/4"
f=open(traj_file);
line=f.readline();
while(line!=""):
    while(line!="-------------\n"):
        line=line.split(" ");
        print line
        draw_circle(src_path,dest_path,line)
        line=f.readline();

    line=f.readline();



















