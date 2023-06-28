import cv2
import imutils  #image video related tasks done by imutils.
im=cv2.imread(r'C:\Users\011382\Desktop\Temp\python.png')
im2=cv2.blur(im,(60, 60)) #blur image (image name, blur weight)
cv2.imshow('output',im2) #image show output image title and image name
key=cv2.waitKey(3000)




image2=cv2.imread(r'C:\Users\011382\Desktop\Temp\python1.png')
image2_resize=imutils.resize(image2,100,100) # imutils package also has resize funtion same as cv2(computer vision)
cv2.imshow('output2',image2_resize)
cv2.imwrite(r'C:\Users\011382\Desktop\Temp\python3.png',image2_resize) #image write to the directory ...location and image name do you want to write
key=cv2.waitKey(3000)



gassianBlur=cv2.GaussianBlur(im,(5,5),cv2.BORDER_DEFAULT)

cv2.imwrite(r'C:\Users\011382\Desktop\Temp\python4.png',gassianBlur)
cv2.imshow('outputgassian',gassianBlur)
key=cv2.waitKey(3000)


imgThresold=cv2.imread(r'C:\Users\011382\Desktop\Temp\python.png')
ret,setImgThresold=cv2.threshold(imgThresold,50,255,cv2.THRESH_BINARY)
#cv2.imshow('Binary Threshold',setImgThresold)
cv2.imwrite(r'C:\Users\011382\Desktop\Temp\python7.png',setImgThresold)



getImagetoGrayScale =  cv2.imread(r'C:\Users\011382\Desktop\Temp\python.png')
setImageGrayScale = cv2.cvtColor(getImagetoGrayScale,cv2.COLOR_BGR2GRAY)
cv2.imshow('GrayScaleImage',setImageGrayScale)
cv2.imwrite(r'C:\Users\011382\Desktop\Temp\python6.png',setImageGrayScale)
key=cv2.waitKey(3000)


# find contours.... this connected edges of the picture.
findImageForContours=cv2.imread(r'C:\Users\011382\Desktop\Temp\python.png') # open the image
covertToGray=cv2.cvtColor(findImageForContours,cv2.COLOR_BGR2GRAY) # convert that image to gray scale
edge=cv2.Canny(covertToGray,30,30) #find canny edges
#cv2.waitKey(0)
contours, hierarchy = cv2.findContours(edge,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # find contours using edges
cv2.imwrite(r'C:\Users\011382\Desktop\Temp\python12.png',edge) #write image with gray scale

imageWithContours=cv2.drawContours(findImageForContours, contours, -1, (0, 255, 0), 3) #draw contours image based on contours find
cv2.imwrite(r'C:\Users\011382\Desktop\Temp\python13.png',imageWithContours)
#cv2.imshow('Canny Edges After Contouring',edge)

#cv2.waitKey(0)
