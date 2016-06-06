import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

#src_dir="/home/ranjan/Kaggle/dense_tracker_ECCV10/moseg/data/UCSD_Anomaly/UCSDped2/Train_block/"


src_dir="/media/ranjan/PART-EXT1/anomaly_detection_data/UCSD_Anomaly/UCSDped2/Train_block/"
DIR_L=os.listdir(src_dir)
DIR_L.sort()
#converts string list to  numpy float64 array 
def convert_List(L):
    L1=[]

    for i in range(0,len(L),2):
        l=L[i];
        l=l.replace("\n","")
        l=l.replace("(","")
        l=l.replace(")","")
        l=l.split(",");
        L1.append((float(l[0]),float(l[1])))

    l=L[-1]
    l=l.replace("\n","")
    l=l.replace("(","")
    l=l.replace(")","")
    l=l.split(","); 
    L1.append((float(l[0]),float(l[1])))


    L1=np.array(L1);
    return(L1)



def dict(D,key,a):
    if(D.has_key(key)):
        D[key]=D[key]+a
    else:
        D[key]=a

    return(D)

#finde difference of vectors
def ux_vy(L,D):
    L1=[]
    for i in range(len(L)-1):
        L1.append( L[i+1]-L[i])

    L1=np.array(L1);


    avg_diff=np.sum(L1,axis=0)/len(L)
    if(abs(np.sum(avg_diff))>0.1):
        #print avg_diff  
        #print "+"
        D=dict(D,blk_no,1)
    else:
        #print "-"
        D=dict(D,blk_no,-1)
    return(L1,D)




#find difference of vectors
def ux_vy1(L):
    L1=[]
    for i in range(len(L)-1):
        L1.append( L[i+1]-L[i])
        l=L[i+1]-L[i]
        #print l[0],l[1]
    L1=np.array(L1);
    if(len(L1)>10):
        #plt.plot(L1[:,0], L1[:,1], 'ro')
        #plt.show()
        #plt.pause(0.0001)
        pass 

    
    #print L1
    #print np.sum(np.std(L1,axis=0)),len(L)
    if(len(L)>5):
        plt.plot(np.std(L1,axis=0)[0],np.std(L1,axis=0)[1], 'ro')
        print    np.std(L1,axis=0)[0],np.std(L1,axis=0)[1]
        plt.pause(0.0000001)

    print "-----"




















def variance(L):
    if(len(L)>15):
        print np.var(L)



blk_no=0
D={}
DIR_L=["1487_4x7.txt"]

for l in DIR_L:
    file1=src_dir+l
    f1=open(file1,"r");
    s=f1.readline(); 
    L=[]
    flag=1;
    blk_no=int(l.split("_")[0])
    #print "---",blk_no,"---"
    
    
    #for each block 
    while(s!=""):
        if(s.find("---")==-1):
            flag=0
            s1=f1.readline(); 
            L.append(s)
            L.append(s1)
        else:

            #each trajectory in a block
            if(flag==0):
                L=convert_List(L)       #convert L into numpy
                #L_uv,D=ux_vy(L,D)
                ux_vy1(L)
                #print L;                   

                #set L to blanck so that it can consider next trajectory
                L=[]

                
            flag=1;
            
        s=f1.readline();
        
    exit()
    #print "------",l,"-------------" 

BLOCK_SIZE_X=7
BLOCK_SIZE_Y=4

IMAGE_SIZE_X=360    #number of pixel along horizontal direction i.e number  of col
IMAGE_SIZE_Y=240    #number of pixel along vertical direction i.e number of row
NUM_BLOCK_X=IMAGE_SIZE_X/BLOCK_SIZE_X
NUM_BLOCK_Y=IMAGE_SIZE_Y/BLOCK_SIZE_Y



img=cv2.imread("/media/ranjan/PART-EXT1/anomaly_detection_data/UCSD_Anomaly/UCSDped2/Train/Train001/001.tif")

#print D



#it find the image coordinate(not geometric coordinate) from the block number 
def find_xy(d):
    x=int(d/(IMAGE_SIZE_X/BLOCK_SIZE_X))
    y=d%(IMAGE_SIZE_X/BLOCK_SIZE_X)
    x=x*BLOCK_SIZE_Y
    y=y*BLOCK_SIZE_X

    return((x,y)) 




for d in D:
    x=int(d/(IMAGE_SIZE_X/BLOCK_SIZE_X))
    y=d%(IMAGE_SIZE_X/BLOCK_SIZE_X)
    x=x*5
    y=y*5
    #print D[d]>0,x,y  
    if(D[d]>0):
        for i in range(5):
            for j in range(5):
                img[x+i][y+j]=(0,0,255)
    else:
        for i in range(5):
            for j in range(5):
                img[x+i][y+j]=(255,0,0)




cv2.imshow("sad",img);
cv2.waitKey(0);


