import cv2 as cv  #引入OpenCV库
image=cv.imread('image.jpg')   #读取图像
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)  #根据图像大小创建窗口
cv.imshow('input_image', image)  #在窗口中显示图像
cv.waitKey(0)  #无限延时等待用户按键事件
cv.destroyAllWindows()  #关闭所有窗口
