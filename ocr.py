from PIL import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
path = r'C:\Users\Timot\Documents\Image-to-Data\DL-1.JPG'
import cv2
import numpy as np

path = 'form.jpg'
# img = cv2.imread(path)
# norm_img = np.zeros((img.shape[0], img.shape[1]))
# img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
# cv2.imshow('image',img)



# data = Image.fromarray(out_binary)
# data.show()
# print(pytesseract.image_to_string(Image.open(path)))
print(pytesseract.image_to_string(Image.open(path)))

class Image_to_Data:
    """
    Class implements pytesseract to transform paper forms to digital. 
    Then uses pandas to make csv database.
    """
    def __init__(self, path, out_file = "image_to_data.csv"):
        """
        Initializes class with images' folder path and outfile.
        """
        self.out_file = out_file
        self.path = path
        return
    def preprocess(self):
        """
        Preprocesses image file to account for noise, text skewing and lighting
        """
        return
    def char_rec(self):
        """
        Runs character recognition program.
        """
        return
    def text_to_database(self):
        """
        Takes key information from recognition and inputs into database
        """
        return

I2D = Image_to_Data(path)
I2D()

# # In order to bypass the image conversions of pytesseract, just use relative or absolute image path
# # NOTE: In this case you should provide tesseract supported images or tesseract will return error
# print(pytesseract.image_to_string('test.png'))

# # List of available languages
# print(pytesseract.get_languages(config=''))

# # French text image to string
# print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))

# # Batch processing with a single file containing the list of multiple image file paths
# print(pytesseract.image_to_string('images.txt'))

# # Timeout/terminate the tesseract job after a period of time
# try:
#     print(pytesseract.image_to_string('test.jpg', timeout=2)) # Timeout after 2 seconds
#     print(pytesseract.image_to_string('test.jpg', timeout=0.5)) # Timeout after half a second
# except RuntimeError as timeout_error:
#     # Tesseract processing is terminated
#     pass

# # Get bounding box estimates
# print(pytesseract.image_to_boxes(Image.open('test.png')))

# # Get verbose data including boxes, confidences, line and page numbers
# print(pytesseract.image_to_data(Image.open('test.png')))

# # Get information about orientation and script detection
# print(pytesseract.image_to_osd(Image.open('test.png')))

# # Get a searchable PDF
# pdf = pytesseract.image_to_pdf_or_hocr('test.png', extension='pdf')
# with open('test.pdf', 'w+b') as f:
#     f.write(pdf) # pdf type is bytes by default

# # Get HOCR output
# hocr = pytesseract.image_to_pdf_or_hocr('test.png', extension='hocr')

# # Get ALTO XML output
# xml = pytesseract.image_to_alto_xml('test.png')
