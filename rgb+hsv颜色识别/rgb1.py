#normal images
import cv2
import numpy as np

def rgb_color_detection(image):
    # 将图像转换为RGB颜色空间（默认即为BGR）
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # 定义颜色范围（这里仅作为示例，实际应用中需要根据具体情况调整）
    color_boundaries = {
        'white': ([200, 200, 200], [255, 255, 255]),
        'black': ([0, 0, 0], [30, 30, 30]),
        'red': ([150, 0, 0], [255, 100, 100]),
        'green': ([0, 150, 0], [100, 255, 100]),
        'blue': ([0, 0, 150], [100, 100, 255]),
        'yellow': ([150, 150, 0], [255, 255, 100])
    }
    
    for name, (lower, upper) in color_boundaries.items():
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)
        
        print(f"Detected {name} pixels: {cv2.countNonZero(mask)}")
        # 显示结果图像
        cv2.imshow(f"Filtered {name}", output)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 加载图像

image = cv2.imread('0_cropped.jpg') #imread('your_image_path_here.jpg')
rgb_color_detection(image)