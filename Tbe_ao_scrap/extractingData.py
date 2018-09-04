
# traitement .docx files


import win32com.client as win32
word = win32.Dispatch("word.Application")
word.Visible = 0 
word.Documents.Open("C:\\Users\Taoufik\Documents\Python Scripts\\4-Bordereau des prix détail estimatif -BPDE-.docx")
doc = word.ActiveDocument
x = doc.Tables.count 
table = doc.Tables(1)
table.Cell(Row = 1, Column= 1)
x = table.Cell(Row =1, Column =1).Range.Text
print(x)




# for filename in os.listdir("C:\\Users\Taoufik\Downloads\\test"):#
#     if os.path.isdir(filename):
#         print('################')
#         print("###  "+filename+"  ###")
#         # traitement .docx files
#         import win32com.client as win32
#         word = win32.Dispatch("word.Application")
#         word.Visible = 0 
#         word.Documents.Open("C:\\Users\Taoufik\Documents\Python Scripts\\4-Bordereau des prix détail estimatif -BPDE-.docx")
        
#         doc = word.ActiveDocument
        
#         x = doc.Tables.count 
        
#         table = doc.Tables(1)
#         table.Cell(Row = 1, Column= 1)
#         x = table.Cell(Row =1, Column =1).Range.Text




#traitement des fichiers pdf

import pytesseract
import pyautogui
import cv2 
import numpy
import PIL
from PIL import Image

import pdf2image
import os 
from os import path

if not os.path.exists('test'):
       os.makedirs('test')
os.chdir("C:\\Users\Taoufik\Documents\Python Scripts\\test")
images = pdf2image.convert_from_path(os.path.join('C:\\Users\Taoufik\Documents\Python Scripts','CPS_ Maintenance.pdf'))
i = 1
for page in images:
    page.save('page'+str(i)+'.jpg', 'JPEG')
    i += 1
print(pytesseract.image_to_string(Image.open('page1.jpg'),lang='fra'))

