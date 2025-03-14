import cv2
import numpy as np

# 定义各种颜色的RGB范围
color_ranges = {
    'white': [(200, 200, 200), (255, 255, 255)],
    'red': [(130, 0, 0), (255, 60, 60)],
    'blue': [(0, 0, 130), (60, 60, 255)],
    'yellow': [(200, 200, 0), (255, 255, 60)],
    'green': [(0, 130, 0), (60, 255, 60)],
    'black': [(0, 0, 0), (60, 60, 60)]
}

def detect_colors(frame):
    detected_colors = []
    
    for color_name, (lower_bound, upper_bound) in color_ranges.items():
        mask = cv2.inRange(frame, np.array(lower_bound), np.array(upper_bound))
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        if len(contours) > 0:
            detected_colors.append(color_name)
            
    return detected_colors

# 读取图片
frame = cv2.imread('0_cropped.jpg')#'path_to_your_image.jpg' 

if frame is None:
    print("Error: Could not read the image.")
else:
    colors = detect_colors(frame)
    text = ', '.join(colors)
    cv2.putText(frame, f'Detected Colors: {text}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # 显示结果
    cv2.imshow('Color Detection', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



