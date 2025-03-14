import cv2
import numpy as np

# 定义各种颜色的HSV范围
color_ranges = {
    'white': [[(0, 0, 180), (180, 30, 255)]],
    'red': [[(0, 120, 70), (10, 255, 255)], # 红色的低阈值
            [(160, 120, 70), (180, 255, 255)]], # 红色的高阈值
    'blue': [[(100, 150, 0), (140, 255, 255)]],
    'yellow': [[(20, 100, 100), (30, 255, 255)]],
    'green': [[(40, 50, 50), (80, 255, 255)]],
    'black': [[(0, 0, 0), (180, 255, 30)]]
}

def detect_colors(frame):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    detected_colors = []
    
    for color_name, ranges in color_ranges.items():
        combined_mask = None
        for lower_bound, upper_bound in ranges:
            mask = cv2.inRange(hsv_frame, np.array(lower_bound), np.array(upper_bound))
            if combined_mask is None:
                combined_mask = mask
            else:
                combined_mask = cv2.bitwise_or(combined_mask, mask)
        
        contours, _ = cv2.findContours(combined_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
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



