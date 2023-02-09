import cv2
image = cv2.imread("HCMUTE.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Anh", image)
cv2.waitKey()
cv2.destroyAllWindows()