#normal images
import cv2
import numpy as np

def hsv_color_detection(image):
    # 将图像转换为HSV颜色空间
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # 定义颜色范围（这里仅作为示例，实际应用中需要根据具体情况调整）
    color_boundaries_hsv = {
        'white': ([0, 0, 200], [180, 30, 255]),
        'black': ([0, 0, 0], [180, 255, 30]),
        'red': ([0, 100, 100], [10, 255, 255]), # 注意红色可能跨越Hue的0度，需处理这种情况
        'green': ([40, 50, 50], [80, 255, 255]),
        'blue': ([100, 150, 0], [140, 255, 255]),
        'yellow': ([20, 100, 100], [40, 255, 255])
    }
    
    for name, (lower, upper) in color_boundaries_hsv.items():
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        
        mask = cv2.inRange(hsv, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)
        
        print(f"Detected {name} pixels: {cv2.countNonZero(mask)}")
        # 显示结果图像
        cv2.imshow(f"Filtered {name}", output)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 加载图像
image = cv2.imread('0_cropped.jpg')  #imread('your_image_path_here.jpg')
hsv_color_detection(image)