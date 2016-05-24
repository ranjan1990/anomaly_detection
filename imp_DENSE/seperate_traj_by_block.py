import os
import resource
hard=4096
resource.setrlimit(resource.RLIMIT_NOFILE, (4096, hard))


src_folder="/home/ranjan/Kaggle/dense_tracker_ECCV10/moseg/data/UCSD_Anomaly/UCSDped2/Train_traj/"
dest_folder="/home/ranjan/Kaggle/dense_tracker_ECCV10/moseg/data/UCSD_Anomaly/UCSDped2/Train_block/"
L=os.listdir(src_folder)
print L
BLOCK_SIZE_X=5
BLOCK_SIZE_Y=5
IMAGE_SIZE_X=360
IMAGE_SIZE_Y=240



#for each block we have a file and for each file we have a file descriptor
#open file descriptor row wise  and return list
def initialize():
    if(IMAGE_SIZE_X%BLOCK_SIZE_X!=0):
        print "try different block size"
        exit();
    if(IMAGE_SIZE_Y%BLOCK_SIZE_Y!=0):
        print "try different block size"
        exit();
    
    list_length=IMAGE_SIZE_X*IMAGE_SIZE_Y/(BLOCK_SIZE_X*BLOCK_SIZE_Y);
    L=[]
    for l in range(list_length):
        f=open(dest_folder+str(l)+"_5x5.txt","w")
        L.append(f);


    return(L);


#close all the files
def close_file(L):
    for f in L:
        f.close();





#from the (x,y) chose a  block i.e file descriptor and return position in the list.
def decide_file_des((x,y)):
    i=x/BLOCK_SIZE_X
    j=y/BLOCK_SIZE_Y
    i=int(i)
    j=int(j)


    num_block_in_col=IMAGE_SIZE_Y/BLOCK_SIZE_Y
    
    #position of file des in a list
    pos_file_des=num_block_in_col*i+j
    return(int(pos_file_des));


#return ((112.000000,2.000000),(112.009262,1.956928)) from -> '(112.000000,2.000000),(112.009262,1.956928) \t \n' 
def process_line(s):
    s=s.replace(" \t \n","");
    s=s.split("),(")
    s1=s[0]
    s2=s[1]
    s1=s1.replace("(","");
    s2=s2.replace(")","");
    s1=s1.split(",")
    s2=s2.split(",")
    x1=float(s1[0])
    y1=float(s1[1])
    x2=float(s2[0])
    y2=float(s2[1])
    return(((x1,y1),(x2,y2)));










file_des_list=initialize()

print "DBG1"
for l in L:
    file1=src_folder+l
    f_file1=open(file1,"r");
    s=f_file1.readline();
   
    i=0;
    old_block_num=new_block_num=-1
    #while(s!="------------------------------\n"):
    while(s!=""):
        if(s.find("---")==-1):
            (p1,p2)=process_line(s)
            new_block_num=decide_file_des(p1)
            if(new_block_num!=old_block_num):
                #print "DBG",new_block_num
                f1=file_des_list[new_block_num];
                f1.write("---\n");

            f=file_des_list[new_block_num];
            f.write(str(p1)+"\n")
            f.write(str(p2)+"\n")
            old_block_num=new_block_num;
    



                
        else:
            #write "---" to the file whose block number is new_block_num
            f1=file_des_list[new_block_num];
            f1.write("---\n");

            old_block_num=new_block_num=-1

        s=f_file1.readline();
        i=i+1
 
    f_file1.close()
    

    close_file(file_des_list);
    exit()














