P=/home/ranjan/Kaggle/dense_tracker_ECCV10/moseg/data/UCSD_Anomaly/UCSDped1/Test/

for d in  `ls $P`
do
     dir1=$P$d
     echo  $dir1
     python find_traj_cluster.py  $dir1
 done

