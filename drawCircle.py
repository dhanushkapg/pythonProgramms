import cv2
import numpy as np

imageDrawCircle=cv2.imread(r'C:\Users\011382\Desktop\Temp\python.png')
imageAfterDraw=cv2.rectangle(imageDrawCircle,(0,0),(500, 500),(255, 0, 0),2)#image,starting points, end points,color, line thinkness
cv2.imwrite(r'C:\Users\011382\Desktop\Temp\python9.png',imageAfterDraw)

imageDrawCircle=cv2.imread(r'C:\Users\011382\Desktop\Temp\python.png')
imageAfterDraw=cv2.circle(imageDrawCircle,(250,250),100,(255, 0, 0),2) #imageName(want to draw),Circle starting point,radius,color,thinkness
cv2.imwrite(r'C:\Users\011382\Desktop\Temp\python10.png',imageAfterDraw)


## write a image on the text

imageToWriteText=cv2.imread(r'C:\Users\011382\Desktop\Temp\python.png')
imageAfterWriteText=cv2.putText(imageToWriteText,'Dhanushka',(300,300),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)
#(imageName,Text,text buttom point, font style, font size, color, line thickness, line type)
cv2.imwrite(r'C:\Users\011382\Desktop\Temp\python11.png',imageAfterWriteText)