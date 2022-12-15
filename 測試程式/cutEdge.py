import numpy as np
import cv2

img = cv2.imread('pic\\plate.png')
cv2.imshow("img",img)
#erode = cv2.erode(img, None, iterations=2)
#cv2.imshow('erode',erode)
height, width = img.shape[:2]
v = [0]*width
z = [0]*height
a = 0
hfg = [[0 for col in range(2)] for row in range(height)]
lfg = [[0 for col in range(2)] for row in range(width)]
box = [0,0,0,0]

for x in range(0, width):
    for y in range(0, height):
        if img[y,x][0] == 0:
            a = a + 1
        else :
            continue
    v[x] = a
    a = 0
l = len(v)
emptyImage = np.zeros((height, width, 3), np.uint8)
for x in range(0,width):
    for y in range(0, v[x]):
        b = (255,255,255)
        emptyImage[y,x] = b
cv2.imshow('chuizhi', emptyImage)

a = 0
emptyImage1 = np.zeros((height, width, 3), np.uint8)
for y in range(0, height):
    for x in range(0, width):
        if img[y,x][0] == 0:
            a = a + 1
        else :
            continue
    z[y] = a
    a = 0
l = len(z)

for y in range(0,height):
    for x in range(0, z[y]):
        b = (255,255,255)
        emptyImage1[y,x] = b
cv2.imshow('shuipin', emptyImage1)

#根据水平投影值选定行分割点
inline = 1
start = 0
end = 0
for i in range(0,height):
    if inline == 1 and z[i] >= 10:  #从空白区进入文字区
        start = i-1  #记录起始行分割点
        print(i)
        inline = 0
    elif (i - start > 3) and z[i] < 1 and inline == 0 :  #从文字区进入空白区
        end = i
        break

inline2 = 1
start2 = 0
end2 = []
c = 0
for i in range(0,width):
    if inline2 == 1 and v[i] >= 1 :  #从空白区进入文字区
        start2 = i-3  #记录起始行分割点
        print(i)
        inline2 = 0
    elif (i - start2 > 3) and v[i] < 10 and inline2 == 0 :  #从文字区进入空白区

        print(i)


#cv2.rectangle(img,(0,start),(width,end),(255,0,0),2)
img = img[0:end, start2:width-5]
cv2.namedWindow('cut',0)
cv2.imshow('cut',img)
cv2.imwrite('pic/plated.png',img)
cv2.waitKey(0)
#cv2.imwrite('pic\\plate.png',img)


