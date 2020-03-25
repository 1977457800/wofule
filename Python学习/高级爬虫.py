from PIL import Image
import pytesseract
img=Image.open('u=1320441599,4127074888&fm=26&gp=0.jpg')

print(pytesseract.image_to_string(img))
