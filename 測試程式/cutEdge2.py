
import cv2
import numpy as np

binary_threshold = 190
segmentation_spacing = 0.8
# 1、讀取影象，並把影象轉換為灰度影象並顯示
img = cv2.imread('pic\\1.PNG')
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.waitKey(0)

# 2、將灰度影象二值化
img_thre = img_gray
cv2.threshold(img_gray, binary_threshold, 255, cv2.THRESH_BINARY, img_thre)
# 3、儲存黑白圖片
cv2.imwrite('pic\\thre_res.png',img_thre)



# # 4、分割字元
# hwhite = [] # 記錄每一列的白色畫素總和
# hblack = [] # .............黑色.......
# height = img_thre.shape[0]
# width = img_thre.shape[1]
# #print(width, height)
# hwhite_max = 0
# hblack_max = 0
# # 計算每一列的黑白色畫素總和
# for i in range(height):
#     hw_count = 0 # 這一列白色總數
#     hb_count = 0 # 這一列黑色總數
#     for j in range(width):
#         if img_thre[i][j] == 255:
#             hw_count += 1
#         else:
#             hb_count += 1
#     hwhite_max = max(hwhite_max, hw_count)
#     hblack_max = max(hblack_max, hb_count)
#     hwhite.append(hw_count)
#     hblack.append(hb_count)
#
# #print('black:',hblack)
# #print('white:',hwhite)
# cv2.imshow('threshold', img_thre)
#
# #切割上下白邊
# hbcount = [] #黑點佔整列的比例
# #b09 = []
#
# for i in range(0,height):
#     hbcount.append(hblack[i]/width)
# #print('b/(b+w):',bcount)
# #如果黑點比例小於0.9大於0.2 記錄此列
# for i in range(0, height):
#     if (hbcount[i] < 0.9 and hbcount[i] > 0.2):
#         hstart = i
#         break
# #print(hstart)
# img = img[hstart:height,:] #將紀錄的那列到最後一列剪下
# img_thre = img_thre[hstart:height,:]
# height = img.shape[0]
# #如果黑點比例大於0.9 記錄此列
# for j in range(0, height):
#     if(hbcount[j+hstart]>0.9):
#         hend = j+hstart
#         break
# img = img[0:hend,:] #將第一列到紀錄的那列剪下
# img_thre = img_thre[0:hend,:]
#
#
# cv2.namedWindow('threshold2',0)
# cv2.imshow('threshold2',img_thre)
# vwhite = [] # 記錄每一行的白色畫素總和
# vblack = [] # .............黑色.......
# height = img.shape[0]
# width = img.shape[1]
# print(width, height)
# vwhite_max = 0
# vblack_max = 0
# # 計算每一行的黑白色畫素總和
# for i in range(width):
#     vw_count = 0 # 這一行白色總數
#     vb_count = 0 # 這一行黑色總數
#     for j in range(height):
#         if img_thre[j][i] == 255:
#             vw_count += 1
#         else:
#             vb_count += 1
#     vwhite_max = max(vwhite_max, vw_count)
#     vblack_max = max(vblack_max, vb_count)
#     vwhite.append(vw_count)
#     vblack.append(vb_count)
#
# print('black:',vblack)
# print('white:',vwhite)
#
# #切割左右白邊
# vbcount = [] #黑點佔整列的比例
# #b09 = []
#
# for i in range(0,width):
#     vbcount.append(vblack[i]/height)
# print('b/(b+w):',vbcount)
#
# #如果黑點比例小於0.9大於0.2 記錄此列
# cl = 0
# vstart = 0
# for i in range(0, width):
#
#     if (vbcount[i] < 0.95 and vbcount[i] > 0):
#         cl+=1
#     print('i,v,c,c/w:', i, vbcount[i], cl, cl/width)
#     if((cl / width) < 0.08 and vbcount[i] > 0.95):
#         cl = 0
#     elif((cl / width) > 0.08) and vbcount[i] > 0.95:
#         print('ok')
#         vstart = i-cl
#         break
#
# print('vstart',vstart)
# img = img[:,vstart:width] #將紀錄的那列到最後一列剪下
# width = img.shape[1]
# print('width:',width)
# #如果黑點比例大於0.9 記錄此列
#
# cr = 0
# vend = 0
# for j in range(width-1,-1,-1):
#
#     if (vbcount[j + vstart] < 0.95 and vbcount[j + vstart] > 0):
#         cr+=1
#     #print('j,v,c,c/w:', j, vbcount[j + vstart], cr, cr/width)
#     if((cr / width) < 0.08 and vbcount[j + vstart] > 0.95):
#         cr = 0
#     elif((cr / width) > 0.08) and vbcount[j + vstart] > 0.95:
#         print('ok')
#         vend = j + cr
#         break
# img = img[:,0:vend] #將第一列到紀錄的那列剪下
# cv2.imwrite("pic\\plated.png",img)
#
# cv2.imshow('h', img)
# cv2.waitKey(0)
