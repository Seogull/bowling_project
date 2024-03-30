import pytesseract
from PIL import Image

image = Image.open('test3.jpg')

text = pytesseract.image_to_string(image, lang='eng')

print(text)