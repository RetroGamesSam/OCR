import os
import re

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

print(os.listdir("./pic"))
# Timeout/terminate the tesseract job after a period of time

txt_folder = "./txt/"
pic_folder = "./pic/"
try:
    for element in os.listdir(pic_folder):
        # print(txt_folder+element+'.txt') # Debug
        text = (pytesseract.image_to_string(pic_folder+element, lang='deu', timeout=5)) # Timeout after 5 seconds
        with open(txt_folder+element+'.txt', 'w', encoding="utf-8") as file:
            file.write(text+'\n')
except RuntimeError as timeout_error:
    # Tesseract processing is terminated
    pass


# Get a searchable PDF 
"""
pdf = pytesseract.image_to_pdf_or_hocr('Feel_1.jpg', extension='pdf')
with open('test.pdf', 'w+b') as file:
    file.write(pdf) # pdf type is bytes by default
"""