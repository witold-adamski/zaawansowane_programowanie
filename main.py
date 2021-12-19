import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program ' \
                                        r'Files\Tesseract-OCR\tesseract.exe '


def read_text(path):
    return pytesseract.image_to_string(cv2.imread(path))
#
# print(read_text('tekst.jpeg'))
# print('//////////////////////////////')
# print(read_text('test2.jpg'))
# print('//////////////////////////////')
# print(read_text('205629.png'))
# print('//////////////////////////////')
# print(read_text('maxresdefault.jpg'))
# print('//////////////////////////////')
# print(read_text('lorem.jpg'))


img = cv2.imread('captcha.JPG')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

converted_img = cv2.threshold(cv2.GaussianBlur(img, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
print(pytesseract.image_to_string(converted_img))

c2 = cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
print(pytesseract.image_to_string(c2))

c3 = cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
print(pytesseract.image_to_string(c3))

c4 = cv2.adaptiveThreshold(cv2.GaussianBlur(img, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
print(pytesseract.image_to_string(c4))

c5 = cv2.adaptiveThreshold(cv2.bilateralFilter(img, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
print(pytesseract.image_to_string(c5))

c6 = cv2.adaptiveThreshold(cv2.medianBlur(img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
print(pytesseract.image_to_string(c6))

cv2.imshow('image', c6)
cv2.waitKey(0)
cv2.destroyAllWindows()
