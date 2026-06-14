Automated Quality Inspection using Computer Vision
Introduction

Quality inspection is one of the most important tasks in industrial manufacturing. Manual inspection requires human effort and may produce inconsistent results.

This project implements an automated quality inspection system using Python and OpenCV.

Objective

The objective of this project is to:

Read component images
Compare a good part with a test part
Detect visible defects
Highlight defective regions
Generate PASS or FAIL output
Software Requirements
Ubuntu Linux
Python 3
OpenCV
VS Code
Tools and Libraries
Python

Used for overall implementation.

OpenCV

Used for image processing operations.

Functions used:

cv2.imread()
cv2.cvtColor()
cv2.absdiff()
cv2.threshold()
cv2.findContours()
cv2.contourArea()
cv2.boundingRect()
cv2.rectangle()
cv2.putText()
Methodology
Image Acquisition

Load reference and test images.

Image Preprocessing

Convert images into grayscale.

Difference Calculation

Calculate pixel-wise difference.

Thresholding

Separate defective regions.

Contour Detection

Locate possible defects.

Defect Marking

Draw bounding boxes around defects.

Decision

Generate PASS or FAIL result.

Algorithm
Load images
Convert to grayscale
Calculate image difference
Apply thresholding
Detect contours
Remove noise
Draw bounding boxes
Count defects
Display result
Results

The system successfully detects visible defects and marks them with red rectangles.

The final output includes:

PASS / FAIL status
Number of defects detected
Applications
Industrial inspection
Manufacturing industries
Assembly line monitoring
Smart factories
Automated quality control
Conclusion

This project demonstrates how basic computer vision techniques can automate industrial inspection tasks. The system reduces manual effort and provides a simple solution for identifying visible defects.