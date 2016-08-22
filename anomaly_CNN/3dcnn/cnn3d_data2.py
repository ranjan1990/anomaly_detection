import numpy as np 
from random import randint



#stride needed to get overlap patch
OVERLAP_STRIDE_X=15
OVERLAP_STRIDE_Y=15
OVERLAP_STRIDE_Z=6

#patch size
PATCH_X=32
PATCH_Y=32
PATCH_Z=7


#thresold is % of  1's in volume of (PATCH_X,PATCH_Y,PATCH_Z)
THRESOLD=0.3

#number of output
NUM_OUTPUT=2



#get the shape of input video
input_array=np.load("./input_ped2.npy")
output_array=np.load("./output_ped2.npy")
[_,Z,Y,X]=input_array.shape


#generate index along X,Y,Z
x=np.r_[:X-PATCH_X:OVERLAP_STRIDE_X]
y=np.r_[:Y-PATCH_Y:OVERLAP_STRIDE_Y]
z=np.r_[:Z-PATCH_Z:OVERLAP_STRIDE_Z]






#generate patch of size   (PATCH_X,PATCH_Y,PATCH_Z) from the video of size (Z,Y,X)
def generate_input(l):
	input_patches = np.empty((x.size*y.size*z.size,1,PATCH_Z, PATCH_Y,PATCH_X))
	c=0;
	for idx in xrange(x.size):
	    for idy in xrange(y.size):
        	for idz in xrange(z.size):
	            patch = l[z[idz]:z[idz]+PATCH_Z,y[idy]:y[idy]+PATCH_Y,x[idx]:x[idx]+PATCH_X].copy()
        	    input_patches[c,0]=patch;
	            c=c+1
	return input_patches




def generate_output(l):
	output_patches = np.empty((x.size*y.size*z.size,NUM_OUTPUT))
	#output_patches = np.empty((x.size*y.size*z.size, PATCH_Z, PATCH_Y,PATCH_X))
        c=0;
	for idx in xrange(x.size):
            for idy in xrange(y.size):
                for idz in xrange(z.size):
                    patch = l[z[idz]:z[idz]+PATCH_Z,y[idy]:y[idy]+PATCH_Y,x[idx]:x[idx]+PATCH_X].copy()
                    output_patches[c]=np.sum(patch)/(PATCH_X*PATCH_Y*PATCH_Z);
		    			
                    if(np.sum(patch)/(PATCH_X*PATCH_Y*PATCH_Z*255)>THRESOLD):
                    	output_patches[c]=np.array([1,0]);
		    else: 
                    	output_patches[c]=np.array([0,1]);

		    c=c+1
	return output_patches


l=input_array[0]
in1=generate_input(l);
l=output_array[0]
out1=generate_output(l)



print in1.shape








#to select train and test data of equal size

anomaly_index=np.nonzero(np.transpose(out1)[0])[0]
Dlength=len(anomaly_index)*3;


Y_Train=np.empty((Dlength,NUM_OUTPUT))
X_Train=np.empty((Dlength,1, 7, 32, 32))

c=0;
for idx in  anomaly_index:
    Y_Train[c]=out1[idx]
    X_Train[c]=in1[idx]
    c=c+1
while(c<len(anomaly_index)*3):
    idx=randint(0,Dlength-1)
    Y_Train[c]=out1[idx]
    X_Train[c]=in1[idx]
    c=c+1
    





print X_Train.shape
print Y_Train.shape


np.save("in1.npy",X_Train);
np.save("out1.npy",Y_Train);



