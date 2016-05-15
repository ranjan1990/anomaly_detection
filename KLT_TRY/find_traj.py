import numpy as np
import cv2


#image show with normal window
def imshow1(frame):
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow("image",frame);
    cv2.waitKey(20)

#image show uning matplot
def imshow(img):
    from matplotlib import pyplot as plt
    plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()

def get_name(i):
    if(i<10):
        return("00"+str(i)+".tif");
    elif(i<100):
        return("0"+str(i)+".tif");
    elif(i<1000):
        return(str(i)+".tif");



folder_name="/home/ranjan/Kaggle/dense_tracker_ECCV10/moseg/data/UCSD_Anomaly/UCSDped1/Test/Test001/"
file_name=get_name(1);

read_file=folder_name+file_name

# params for ShiTomasi corner detection
feature_params = dict( maxCorners = 1000,
                       qualityLevel = 0.2,
                       minDistance = 7,
                       blockSize = 7 )

# Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (5,5),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Create some random colors
color = np.random.randint(0,255,(100,3))

# Take first frame and find corners in it
old_gray = cv2.imread(read_file,cv2.COLOR_BGR2GRAY)
p1 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)

# Create a mask image for drawing purposes
mask = np.zeros_like(old_gray)
j=1;
while(j<200):
    j=j+1
    file_name = get_name(j)
    read_file=folder_name+file_name;
    frame_gray = cv2.imread(read_file,cv2.COLOR_BGR2GRAY)
    print frame_gray
    #imshow1(frame_gray)

    #raw_input()
    # calculate optical flow
    p2, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p1, None, **lk_params)

    # Select good points
    good_new = p2[st==1]
    good_old = p1[st==1]

    print j
    # draw the tracks
    for i,(new,old) in enumerate(zip(good_new,good_old)):
        a,b = new.ravel()
        c,d = old.ravel()
        mask = cv2.line(mask, (a,b),(c,d), (0,255,0), 2)
        frame = cv2.circle(frame_gray,(a,b),2,(255,0,255),-1)
    img = cv2.add(frame,mask)

    imshow1(img)
    # Now update the previous frame and previous points
    old_gray = frame_gray.copy()
    p1 = good_new.reshape(-1,1,2)
    print j
#cv2.destroyAllWindows()
