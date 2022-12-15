
import cv2

binary_threshold = 120
segmentation_spacing = 0.8
# 1、讀取影象，並把影象轉換為灰度影象並顯示
img = cv2.imread('pic\\plated.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.waitKey(0)

# 2、將灰度影象二值化
img_thre = img_gray
cv2.threshold(img_gray, binary_threshold, 255, cv2.THRESH_BINARY_INV, img_thre)
cv2.imshow('threshold', img_thre)
cv2.waitKey(0)
# 3、儲存黑白圖片
cv2.imwrite('pic\\thre_res.png',img_thre)
# 4、分割字元
white = [] # 記錄每一列的白色畫素總和
black = [] # .............黑色.......
height = img_thre.shape[0]
width = img_thre.shape[1]
print(width, height)
white_max = 0  
black_max = 0   
# 計算每一列的黑白色畫素總和
for i in range(width):
    w_count = 0 # 這一列白色總數
    b_count = 0 # 這一列黑色總數
    for j in range(height):
        if img_thre[j][i] == 255:
            w_count += 1
        else:
            b_count += 1
    white_max = max(white_max, w_count)
    black_max = max(black_max, b_count)
    white.append(w_count)
    black.append(b_count)

print(black)
print(white)
arg = black_max > white_max # False表示白底黑字；True表示黑底白字



# 分割影象
def find_end(start_):
    end_ = start_ + 1
    for m in range(start_+1, width - 1):
        if(black[m] if arg else white[m]) > (segmentation_spacing * black_max if arg else segmentation_spacing * white_max):
            end_ = m
            break
    return end_

ap=1
n = 1
start = 1
end = 2
while n < width - 1:
    n += 1
    ap +=1
    if(white[n] if arg else black[n]) > ((1 - segmentation_spacing) * white_max if arg else (1 - segmentation_spacing) * black_max):
        # 上面這些判斷用來辨別是白底黑字還是黑底白字
        # 0.05這個引數請多調整，對應上面的0.95
        start = n
        end = find_end(start)
        n = end
        if end - start > 5:
            print(start, end)
            cj = img_thre[1:height, start:end]
            cv2.imwrite('pic\\img/{0}.png'.format(n), cj)
            cv2.imshow('cutChar', cj)
            path = 'pic\\cut\\cut'
            cv2.imwrite(str(path)+str(ap)+'.png',cj)

            cv2.waitKey(0)