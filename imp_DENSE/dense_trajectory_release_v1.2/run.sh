

folder=/home/ranjan/Kaggle/dense_tracker_ECCV10/moseg/data/UCSD_Anomaly/UCSDped2/Test_video/
folder_T=/home/ranjan/Kaggle/dense_tracker_ECCV10/moseg/data/UCSD_Anomaly/UCSDped2/Test_traj/
for vid in `ls $folder`
do
  vid_file=$folder$vid

  vid_file_t=$folder_T"T_"$vid".txt"
  echo $vid_file_t
  ./release/DenseTrack $vid_file >$vid_file_t 
  #./release/Video $vid_file
done



