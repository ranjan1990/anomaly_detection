import cv2
import numpy as np
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






for i in range(1,200):
    file_name=get_name(i)
    print file_name
    frame1=cv2.imread("Test001/"+file_name);
    frame_dis=cv2.imread("Test001/"+file_name);
    """ 
    #detect key point wih mask
    M=np.zeros(frame1.shape[:-1],dtype=np.uint8)
    Mask_with_one(M,(5,5),(i1,j1))   
    sift = cv2.xfeatures2d.SIFT_create()
    kp = sift.detect(frame1,M)
    """   
       
    sift = cv2.xfeatures2d.SIFT_create()
    kp = sift.detect(frame1,None)
    
    
    print len(kp)
    display_keypoint_in_image(frame1,kp)


