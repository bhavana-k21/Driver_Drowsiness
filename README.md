# Driver_Drowsiness
To develop a system that able to detect drowsiness of a driver based on eyelid detection in digital image.

ABSTRACT

Nowadays, more and more professions require concentration. Drivers must keep a close eye on the road, so they can react to sudden events immediately. Driver fatigue often becomes a direct cause of many traffic accidents. Therefore, there is a need to develop the systems that will detect and notify a driver of her/him bad psychophysical condition, which could significantly reduce the number of fatigue-related car accidents. However, the development of such systems encounters many difficulties related to fast and proper recognition of a driver’s fatigue symptoms. One of the technical possibilities to implement driver drowsiness detection systems is to use the vision-based approach. This project presents the currently used driver drowsiness detection systems. The technical aspects of using the vision system to detect driver drowsiness are also discussed.

PROBLEM DEFINITION

This project is to develop a driver drowsiness detection system by using histogram analysis on oriented gradients of Image. It is known that a driver is under drowsiness influences by looking at the eyelid. Based on the previous research, very less researchers have used histogram for analysis. The result will not be accurate, because histogram analysis analyzed the whole image. Therefore, if the analysis area is not specified, the result will not be accurate.

AIM AND OBJECTIVE

i) To develop a system that able to detect drowsiness of a driver based on eyelid detection in digital image. ii) To make analysis of the eyelid by using Euclidian distance between eyes.

BENEFITS

• Using this, we can detect symptoms of driver fatigue early to avoid accidents. • System can be developed at low cost. • Sensors are sensitive enough to detect minor movements. • Area required for installation is less, can be fitted to small places in car. • No manual attention is needed. • Automatically controlled and easy to use.

INTRODUCTION TO TECHNOLOGY USED

PYTHON JUPYTER NOTEBOOK APP NOTEBOOK DOCUMENT

WORKING

A program was developed to identify the driver's drowsiness based on real-time camera image and image processing techniques. This program makes warning through alarm, when it detects drowsiness driving. Extracting face and eye region: Using the Histogram Oriented Gradients face pattern, to find the face from the Grayscaled-HOG-input-image. Use the Face Landmark Estimation algorithm to locate the landmarks on the face.

Drowsiness detection method:Each eye is represented by 6 (x, y)-coordinatesThe Eye Aspect Ratio (EAR) is calculated using six (x, y) coordinates for the detected eye.

• The calculated EAR will have a value more than zero when the eyes are open, and a value close to zero when the eyes are closed. • This program has set a 50% value from the average EAR value to the threshold value.

measures the average EAR value when the eyes are open.
measures the average EAR value when the driver is closing his eyes
sets the threshold using the above two results.
• The computed EAR has a nonzero value when you open your eyes and a value close to zero when you close your eyes. If you set a certain threshold to the threshold (the threshold used to determine drowsy operation), you can detect that the driver is drowsy by checking whether the EAR value is smaller than that value. • In addition, since it is not necessary to examine both eyes separately to determine drowsy driving, the average of EAR values of each eye was used. • Threshold value is set to 50% of EAR value when eyes are opened. If it's smaller (when the eye size is smaller), the driver thinks you're sleepy and cares about whether you're sleepy, so the alarm sounds even if you're not in full sleep. • To apply this algorithm, we applied three steps:

Determine average EAR value when driver opens eyes
Determine average EAR value when driver closes eyes
EAR value that is 50% of eyes open using the above two values. if EAR < threshold for 20 frame then going alarm off.
The drowsiness phase is divided according to the time when the eyes are closed and the time the eyes were opened before the drowsiness operation. To distinguish drowsiness level, we used K-Nearest Neighbor(KNN) supervised learning algorithm.

A non-intrusive system to localize the eyes and monitor fatigue was developed. Information about the face and eyes position are obtained through various algorithms. During the monitoring, the system is able to decide whether the eyes are opened or closed. When the eyes have been closed for few seconds, a warning signal is issued. In addition during monitoring, the system is able to automatically detect any eye localizing error that might have occurred.
