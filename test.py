import cv2
import pytesseract
from PIL import Image
from py_translator import Translator
import os


print("press 1 from camera or press 2 to access from folder(recommended)")

t=int(input())
if t==1:
    #taking the photo
    cap=cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        cv2.imshow('frame',rgb)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            out=cv2.imwrite('sample1.jpg',frame) #mention the path where you want to store the image
            break
    cap.release()
    cv2.destroyAllWindows()
    
    
#tesseract
print("Choose source of image:")

print("    ")

print("Camera 1/ Folder 2")

a=int(input())

if  a is 1:
    img=Image.open('sample1.jpg')
else:
    img=Image.open('sample.png')
    

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
result=pytesseract.image_to_string(img)
#translation

print("Enter the language You want")
print("    ")

print("fr(french),es(spnish),la(latin),sv(swedish)")

print("    ")
s = Translator().translate(result, dest=input()).text#fr(french),es(spnish),la
"""la(latin),sv(swedish)"""
print("    ")
#wrting in file_-_---____-------------____
print("wrting in file_-_---____-------------____")

print("    ")

print("orginal content:")

print("    ")
file=open("file.txt","w")
file.write(result)
file.write(s)
file.close()

print("    ")

print(result)


print("    ")

print("Translated Content:")
print("----------------------------")
print(s)


