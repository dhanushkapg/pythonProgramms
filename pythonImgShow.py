import cv2
from PIL import Image
im = cv2.imread(r'C:\Users\011382\Desktop\Temp\python.png')
#print(im.shape())
print(im.shape) # result of the shape received as tuple
print(im.shape[0])
print(im.shape[1])
#print(im.size)
print(im.dtype) #image Data type default is uint8
imS = cv2.resize(im, (512, 512))
cv2.imshow("output", imS)
key = cv2.waitKey(3000) # change to your own waiting time 1000 = 1 second waitKey(0) means infinite
if key==300: #key is 300 mean check key ==300 thne destroy all windows 
    cv2.destroyAllWindows()

# convert into gray image
image = Image.fromarray(im)
img_gray = image.convert('RGB') # Convert into RGB
img_h = image.convert('L') # convert into Black and White
img_gray.save(r'C:\Users\011382\Desktop\Temp\python1.png')
img_h.save(r'C:\Users\011382\Desktop\Temp\python2.png')
img_gray = cv2.imread(r'C:\Users\011382\Desktop\Temp\python1.png') # open saved image
img_gray = cv2.resize(img_gray, (512, 512)) # resize image
cv2.imshow("output1",img_gray)
key=cv2.waitKey(3000)
if key==500:
    cv2.destroyAllWindows()
