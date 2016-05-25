import os
import numpy as np


#src_dir="/home/ranjan/Kaggle/dense_tracker_ECCV10/moseg/data/UCSD_Anomaly/UCSDped2/Train_block/"
src_dir="/media/ranjan/PART-EXT1/anomaly_detection_data/UCSD_Anomaly/UCSDped1/Train_block/"
DIR_L=os.listdir(src_dir)
DIR_L.sort()


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
    
    
    
    
    
    
    np.array(L1);
    return(L1)

def variance(L):
    L1=convert_List(L)
    if(len(L1)>15):
        print np.var(L1)
    



for l in DIR_L:
    file1=src_dir+l
    f1=open(file1,"r");
    s=f1.readline(); 
    L=[]
    flag=1;
    while(s!=""):
        if(s.find("---")==-1):
            flag=0
            s1=f1.readline(); 
            L.append(s)
            L.append(s1)
        else:
            if(flag==0):
                variance(L);
                #print L
                L=[]



            flag=1;
            
        s=f1.readline();
    print "------",l,"-------------" 


