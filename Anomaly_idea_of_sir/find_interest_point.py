import cv2
import numpy as np
from matplotlib import pyplot as plt

MAX_KEY_POINT=400;


def get_name(i):
    if(i<10):
        return("00"+str(i)+".tif");
    elif(i<100):
        return("0"+str(i)+".tif");
    elif(i<1000):
        return(str(i)+".tif");



#shape=tupple the shape og the rectange . origin coordinate at which  we wan to mask
def Mask_with_one(M,shape,origin_cordiante):
    XO=origin_cordiante[0]-(shape[0])/2
    YO=origin_cordiante[1]-(shape[1])/2

    XD=shape[0]/2+origin_cordiante[0]
    YD=shape[1]/2+origin_cordiante[1]

    if(XD>M.shape[0]):
        XD=XD-(XD-M.shape[0])
        
    if(YD>M.shape[1]):
        YD=YD-(YD-M.shape[1])
    if(XO<0):
        XO=0
    if(YO<0):
        YO=0

    #M[cor[0]:cor[0]+shape[0]].T[cor[1]:cor[1]+shape[1]]=1
    #M[origin_cordiante[0]:XD].T[origin_cordiante[1]:YD]=1
    M[XO:XD+1].T[YO:YD+1]=1
    #print j,XO,XD,YO,YD
    #print M[XO:XD+1].T[YO:YD+1].T





#It draws key point kp and display an image in larger size untill you press NY KWY
def display_keypoint_in_image(frame,kp):
    cv2.drawKeypoints(frame,kp,frame,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    frame_dis= cv2.resize(frame, (714,474))
    cv2.imshow("keypoint",frame_dis)
    cv2.waitKey(1);


def display_image(frame):
    cv2.imshow("frame",frame)
    cv2.waitKey(1);


""" 
    #detect key point wih mask
    M=np.zeros(frame1.shape[:-1],dtype=np.uint8)
    Mask_with_one(M,(5,5),(i1,j1))   
    sift = cv2.xfeatures2d.SIFT_create()
    kp = sift.detect(frame1,M)
"""   
def key_cor(kp1,ind1,kp2,ind2):
    print kp1[ind1].pt
    #print kp2[ind2].pt
    

def get_traj_matrix(KP_DES):

    match_index=np.zeros((MAX_KEY_POINT,len(KP_DES)),dtype=np.int32)
    
    #here I have used brute force method
    bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
    
    #match key point two  consucative frame
    for i in range(len(KP_DES)-1):
        matches = bf.match(KP_DES[i][1],KP_DES[i+1][1])
        matches = sorted(matches,key = lambda x:x.distance)
        
        for m in matches:
            #match_index[m.trainIdx][i]=m.queryIdx
            #for all matches storre it into matrix ith col indicates the 
            #if(m.distance<100):
            match_index[m.queryIdx][i]=m.trainIdx
    return match_index


def traverse_matrix(mat,KP_DES):
    for i in range(MAX_KEY_POINT):
        k=i;
        if(mat[i][0]!=0):
            print"---------------"
        for j in range(len(KP_DES)-1):
            if(mat[k][j]!=0):
                key_cor(KP_DES[j][0],k,KP_DES[j+1][0],mat[k][j])
                k=mat[k][j]
            else:
                break;






for i in range(1,199,1500):
    
    #frame stacked over here
    FRAME=[]
    KP_DES=[]       #this is key point descriptor contains (kp,des) for each frame 
    #considering 3 frame at a time
    for fno in range(i,i+100):
        file_name=get_name(fno)
        frame=cv2.imread("Test001/"+file_name);
        FRAME.append(frame);
        
        sift = cv2.xfeatures2d.SIFT_create()
        #compute descriptor and keypoint
        kp,des = sift.detectAndCompute(frame,None)
        KP_DES.append((kp,des));
        #display_keypoint_in_image(frame,KP_DES[fno-i][0])
          
        
    
    mat=get_traj_matrix(KP_DES)        #get trajectory matrix from Key point and descriptor by matching
    traverse_matrix(mat,KP_DES) 




#    traverse_matrix(mat,KP_DES)


    


 







