import os
import sys

#file_name="/home/ranjan/Kaggle/dense_tracker_ECCV10/moseg/data/UCSD_Anomaly/UCSDped1/Test/Test003/BroxMalikResults/Tracks200.dat"

#dir to store  individual cluster trajectory 
dir1="result_"+sys.argv[1].partition("data/")[-1]
file_name=sys.argv[1]+"/BroxMalikResults/Tracks200.dat"

try:
        os.stat(dir1)
        
except:
        os.makedirs(dir1)       





f=open(file_name,"r");
f.readline()
f.readline()
D={}        #dictionary to get the count of number of tajectory
line=f.readline()
while(line!=""):
    line=line.split()
    t_label=int(line[0])
    t_no=int(line[1]) #numer of trajectory
    if(D.has_key(t_label)):
        D[t_label]= D[t_label]+1
    else:
        D[t_label]=1;

    f1=open(dir1+"/"+str(t_label),"a")
    for i in range(t_no):
        line=f.readline();
        f1.write(line);

    f1.write("-------------\n")
    f1.close()
    line=f.readline()

print D
