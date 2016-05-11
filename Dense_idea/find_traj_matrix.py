file_name="/home/ranjan/Kaggle/dense_tracker_ECCV10/moseg/data/UCSD_Anomaly/UCSDped1/Test/Test001/BroxMalikResults/Tracks200.dat"

f=open(file_name,"r");
f.readline()
f.readline()

while(True):
    line=f.readline()
    line=line.split()
    t_label=int(line[0])
    t_no=int(line[1]) #numer of trajectory
    print t_label
    for i in range(t_no):
        f.readline();
    




