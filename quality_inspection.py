import cv2

REFERENCE_IMAGE = "images/good4.jpeg"
TEST_IMAGE = "images/defective4.jpeg"

reference = cv2.imread(REFERENCE_IMAGE)
test = cv2.imread(TEST_IMAGE)

if reference is None or test is None:
    print("Error: Image not found!")
    exit()

reference_gray = cv2.cvtColor(reference, cv2.COLOR_BGR2GRAY)
test_gray = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)

difference = cv2.absdiff(reference_gray, test_gray)

_, threshold = cv2.threshold(
    difference,
    30,
    255,
    cv2.THRESH_BINARY
)

contours, _ = cv2.findContours(
    threshold,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

defect_found = False
defect_count = 0

for contour in contours:

    area = cv2.contourArea(contour)

    if area > 20:

        defect_found = True
        defect_count += 1

        x, y, w, h = cv2.boundingRect(contour)

        cv2.rectangle(
            test,
            (x, y),
            (x + w, y + h),
            (0, 0, 255),
            2
        )

        cv2.putText(
            test,
            "DEFECT",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 0, 255),
            2
        )

if defect_found:

    cv2.putText(
        test,
        f"FAIL | Defects: {defect_count}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 255),
        2
    )

else:

    cv2.putText(
        test,
        "PASS",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

print("Inspection Complete")
print(f"Defects Found: {defect_count}")

cv2.imshow("Quality Inspection Result", test)

cv2.waitKey(0)
cv2.destroyAllWindows()