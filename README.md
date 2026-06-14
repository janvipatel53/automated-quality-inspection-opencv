# Automated Quality Inspection using Computer Vision

## Overview

This project was developed as part of the Robotics and Automation Industrial Training Program.

The objective of this project is to automate the inspection of mechanical components using Computer Vision techniques. The system compares a reference image with a test image and identifies visible defects automatically.

The project is implemented using Python and OpenCV.

---

## Problem Statement

In manufacturing industries, manual inspection is time consuming and can lead to human errors. This project demonstrates a simple automated quality inspection system that can identify defective parts with the help of image processing.

---

## Features

- Automated defect detection
- Reference and test image comparison
- Grayscale image processing
- Difference image generation
- Thresholding
- Contour detection
- Bounding box generation
- PASS / FAIL classification
- Defect counting

---

## Technologies Used

- Python 3
- OpenCV
- Image Processing

---

## Folder Structure

```
automated-quality-inspection-opencv
│
├── images
│   ├── good1.jpeg
│   ├── good2.jpeg
│   ├── good3.jpeg
│   ├── good4.jpeg
│   ├── defective1.jpeg
│   ├── defective2.jpeg
│   ├── defective3.jpeg
│   └── defective4.jpeg
│
├── quality_inspection.py
├── requirements.txt
├── README.md
└── Documentation.md
```

---

## Working

### Step 1

Load the reference image and test image.

### Step 2

Convert both images into grayscale.

### Step 3

Calculate absolute difference between images.

### Step 4

Apply binary thresholding.

### Step 5

Detect contours.

### Step 6

Ignore small noisy regions.

### Step 7

Draw bounding boxes around defects.

### Step 8

Display PASS or FAIL result.

---

## Installation

Install OpenCV:

```bash
pip install -r requirements.txt
```

or

```bash
pip install opencv-python
```

---

## Run

```bash
python3 quality_inspection.py
```

---

## Output

The system:

- Detects defects
- Draws red bounding boxes
- Counts defects
- Displays PASS or FAIL

---

## Applications

- Industrial Automation
- Manufacturing
- Conveyor Belt Inspection
- Mechanical Component Testing
- Smart Factory Systems
