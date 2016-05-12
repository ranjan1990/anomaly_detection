import cv2
import numpy as np

src_path="/home/ranjan/Kaggle/dense_tracker_ECCV10/moseg/data/UCSD_Anomaly/UCSDped2/Test/Test001/"
dest_path="/home/ranjan/Kaggle/dense_tracker_ECCV10/moseg/data/UCSD_Anomaly/UCSDped2/Test/Test001/"
traj_file="Test001_cluster_traj2/0"

#image show with normal window
def imshow1(frame):
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow("image",frame);
    cv2.waitKey(50)
               
               
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
    cv2.imwrite(traj_file+f_name,img);
#find u,v,anglee
def find_dx_dy_da(t1,t2):
    frame_num=int(float(line[2]))+1 #+1 because frame number statrs from 0
    x=int(float(line[0]))
    y=int(float(line[1]))
        




f=open(traj_file);
line=f.readline();
while(line!=""):
    while(line!="-------------\n"):
        line=line.split(" ");
        print line
        img=draw_circle(src_path,dest_path,line)
                

        line=f.readline();

    line=f.readline();



















