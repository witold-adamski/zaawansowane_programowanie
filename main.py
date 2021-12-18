import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program ' \
                                        r'Files\Tesseract-OCR\tesseract.exe '


def read_text(path):
    return pytesseract.image_to_string(cv2.imread(path))


print(read_text('tekst.jpeg'))
print('//////////////////////////////')
print(read_text('test2.jpg'))
print('//////////////////////////////')
print(read_text('205629.png'))
print('//////////////////////////////')
print(read_text('maxresdefault.jpg'))
print('//////////////////////////////')
print(read_text('lorem.jpg'))
