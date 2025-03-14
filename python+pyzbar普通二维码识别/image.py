import cv2
from pyzbar import pyzbar

def decode_qr_codes(image):
    decoded_objects =pyzbar.decode(image)
    for obj in decoded_objects:
        #打印二维码内容
        print("Type:",obj.type)
        print("Data:",obj.data.decode("utf-8"))
        #获取二维码顶点
        points = obj.polygon
        if len(points) == 4:
            print("QR Code Points:")
            for point in points:
                print(f"({point.x},{point.y})")
            

    
    return image

image = cv2.imread('image2.jpg')

result_image = decode_qr_codes(image)

cv2.imshow('Detected QR Codes',result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

