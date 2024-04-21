import cv2

src = cv2.imread("734154.jpg", cv2.IMREAD_UNCHANGED)
# cv2.imshow("title", src)


# percent wise resizing
scale_percent = 50

# calculating width and height
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[1] * scale_percent / 100)

# show
output = cv2.resize(src, (width, height))
cv2.imwrite('newImg.png', output)

# Wait
cv2.waitKey(0)



