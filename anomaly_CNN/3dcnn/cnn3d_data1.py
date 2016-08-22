#from keras.models import Sequentiail"
#from keras.layers import Dense, Activation;
import cv2
import os
import numpy as np
#import data from ped2 dataset 


#test dir list
D=["/home/ecsuiplab/CNN/UCSD_Anomaly/TEST_DATA/ped2/Test001_gt","/home/ecsuiplab/CNN/UCSD_Anomaly/TEST_DATA/ped2/Test002_gt","/home/ecsuiplab/CNN/UCSD_Anomaly/TEST_DATA/ped2/Test004_gt","/home/ecsuiplab/CNN/UCSD_Anomaly/TEST_DATA/ped2/Test005_gt","/home/ecsuiplab/CNN/UCSD_Anomaly/TEST_DATA/ped2/Test007_gt","/home/ecsuiplab/CNN/UCSD_Anomaly/TEST_DATA/ped2/Test008_gt","/home/ecsuiplab/CNN/UCSD_Anomaly/TEST_DATA/ped2/Test010_gt","/home/ecsuiplab/CNN/UCSD_Anomaly/TEST_DATA/ped2/Test011_gt"]



#dimension along X asxis and Y axis not row col
X_DIM=360
Y_DIM=240
#number of frame per video
NUM_FRAME=150

#number of  video
NUM_SAMPLE=8;




#to get the images of video into  a array and return
def get_images(dir1):
	alimpv=np.zeros((NUM_FRAME,Y_DIM,X_DIM),dtype="uint8")	#all image per video in a single video.
	c=0;
	for i in range(1,NUM_FRAME+1):
		if(i<10):
			fname=dir1+"/00"+str(i)+".bmp"
		elif(i<100):
			fname=dir1+"/0"+str(i)+".bmp"
		elif(i<1000):
			fname=dir1+"/"+str(i)+".bmp"

		#print "fname=",fname	
		frame=cv2.imread(fname);
		image=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)	
		alimpv[c]=image[:,:]

			
		print "alimpv",image
		c=c+1;

	return alimpv	
	

#for tif
def get_images1(dir1):
        alimpv=np.zeros((NUM_FRAME,Y_DIM,X_DIM),dtype="uint8")  #all image per video in a single video.
        c=0;
        for i in range(1,NUM_FRAME+1):
                if(i<10):
                        fname=dir1+"/00"+str(i)+".tif"
                elif(i<100):
                        fname=dir1+"/0"+str(i)+".tif"
                elif(i<1000):
                        fname=dir1+"/"+str(i)+".tif"

                #print "fname=",fname
                frame=cv2.imread(fname);
                image=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		#print image
                alimpv[c]=image[:,:]
                #print "alimpv",image
                c=c+1;

        return alimpv






input_array=np.zeros((NUM_SAMPLE,NUM_FRAME,Y_DIM,X_DIM),dtype="uint8");
output_array=np.zeros((NUM_SAMPLE,NUM_FRAME,Y_DIM,X_DIM),dtype="uint8");


c=0
for dir1 in D:
	out_put_dir=dir1
	input_dir=dir1[:-3]
	input_array[c]=get_images1(input_dir)
	output_array[c]=get_images(out_put_dir)
	c=c+1

	#print "****************",dir1
	
print input_array.shape	
print output_array.shape	
np.save("./input_ped2.npy",input_array)		
np.save("./output_ped2.npy",output_array)		



#generate patch index


input_array=np.load("./input_ped2.npy")


#stride needed to get overlap patch
OVERLAP_STRIDE_X=15
OVERLAP_STRIDE_Y=15
OVERLAP_STRIDE_Z=6

#patch size
PATCH_X=30
PATCH_Y=30
PATCH_Z=12


#get the shape of input video
[_,Z,Y,X]=input_array.shape


#generate index along X,Y,Z
x=np.r_[:X-PATCH_X:OVERLAP_STRIDE_X]
y=np.r_[:Y-PATCH_Y:OVERLAP_STRIDE_Y]
z=np.r_[:Z-PATCH_Z:OVERLAP_STRIDE_Z]




l=input_array[0]

input_patches = np.empty((x.size*y.size*z.size, PATCH_Z, PATCH_Y,PATCH_X))
c=0;

for idx in xrange(x.size):
    for idy in xrange(y.size):
        for idz in xrange(y.size):
            patch = l[z[idz]:z[idz]+PATCH_Z,y[idy]:y[idy]+PATCH_Y,x[idx]:x[idx]+PATCH_X].copy()
            input_patches[c]=patch;
            c=c+1
        
print input_patches.shape


 




