import cv2

def light_removing(frame) :
    imgUMat = cv2.imread(frame)
    gray = cv2.cvtColor(imgUMat, cv2.COLOR_RGB2GRAY)
    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    L = lab[:,:,0]
    med_L = cv2.medianBlur(L,99) #median filter
    invert_L = cv2.bitwise_not(med_L) #invert lightness
    composed = cv2.addWeighted(gray, 0.75, invert_L, 0.25, 0)
    return L, composed

