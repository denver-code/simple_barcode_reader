import cv2

print(cv2.__version__)

bd = cv2.barcode.BarcodeDetector('sr.prototxt', 'sr.caffemodel')

def retval_code(image):
    retval, decoded_info, decoded_type, points = bd.detectAndDecode(image)
    if not retval:
        return "Looks like you have wrong image without proper barcode, please make sure on picture are only one proper barcode"

    return decoded_info[0]

print(retval_code(cv2.imread('2023-03-15 16.58.47.jpg')))