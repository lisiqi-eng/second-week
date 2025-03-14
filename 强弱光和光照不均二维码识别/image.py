import cv2
import numpy as np
from pyzbar.pyzbar import decode

def preprocess_image(image):
    # 转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 应用直方图均衡化以增强对比度
    equalized = cv2.equalizeHist(gray)
    
    # 使用自适应阈值二值化处理
    _, binary = cv2.threshold(equalized, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # 形态学操作：膨胀和腐蚀
    kernel = np.ones((3, 3), np.uint8)
    dilated = cv2.dilate(binary, kernel, iterations=1)
    eroded = cv2.erode(dilated, kernel, iterations=1)
    
    return eroded

def detect_qr_codes(image_path):
    # 读取图像
    image = cv2.imread(image_path)
    
    if image is None:
        print("无法读取图像")
        return
    
    # 预处理图像
    processed_image = preprocess_image(image)
    
    # 解码二维码
    qr_codes = decode(processed_image)
    
    if not qr_codes:
        print("未检测到二维码")
    
    # 显示结果
    for qr_code in qr_codes:
        points = qr_code.polygon
        n_points = len(points)
        
        # 将点转换为整数坐标
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        
        # 绘制多边形边界
        cv2.polylines(image, [pts], True, (0, 255, 0), 5)
        
        # 提取并显示二维码数据
        data = qr_code.data.decode('utf-8')
        x, y = points[0].x, points[0].y
        cv2.putText(image, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        print("QR Code Data:", data)
    
    # 显示原始图像和处理后的图像
    cv2.imshow('Original Image', image)
    cv2.imshow('Processed Image', processed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 示例调用
detect_qr_codes('image1.jpg')



