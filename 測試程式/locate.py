
import cv2
import numpy as np

minPlateRatio = 1.5 #車牌最小比例
maxPlateRatio = 5   #車牌最大比例
binary_threshold = 120 #設定二值化閾值是120
segmentation_spacing = 0.85 #分割間距

# 图像处理
def imageProcess(gray):
    # 高斯濾波
    gaussian = cv2.GaussianBlur(gray, (3, 3), 0, 0, cv2.BORDER_DEFAULT)

    # Sobel運算，求水平梯度
    sobel = cv2.convertScaleAbs(cv2.Sobel(gaussian, cv2.CV_16S, 1, 0, ksize=3))

    # 二值化
    ret, binary = cv2.threshold(sobel, 150, 255, cv2.THRESH_BINARY)

    # 閉操作
    element = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 4))
    closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, element)

    # 再通過腐蝕->膨脹 去掉比較小的噪點
    erosion = cv2.erode(closed, None, iterations=2)
    dilation = cv2.dilate(erosion, None, iterations=3)

    # 回傳圖像
    return dilation

# 找到符合車牌形狀的矩形
def findPlateNumberRegion(img):
    region = []
    # 找尋外框輪廓
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    print("contours lenth is :%s" % (len(contours)))
    # 篩選面積小的
    for i in range(len(contours)):
        cnt = contours[i]
        # 計算輪廓面積
        area = cv2.contourArea(cnt)

        # 忽略面積小的
        if area < 2000:
            continue

        # 轉換成對應矩形（最小）
        rect = cv2.minAreaRect(cnt)
        # print("rect is:%s" % {rect})

        # 根據矩形轉成box類型，並int化
        box = np.int32(cv2.boxPoints(rect))

        # 計算高和寬
        height = abs(box[0][1] - box[2][1])
        width = abs(box[0][0] - box[2][0])
        # 正常情况車牌長高比在1.5~5之间
        ratio = float(width) / float(height)
        if ratio > maxPlateRatio or ratio < minPlateRatio:
            continue
        # 符合條件，加入輪廓
        region.append(box)
    return region

def detect(img):
    # 灰階處理
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('pic\\gray.png', gray)
    # 形態學變換處理
    dilation = imageProcess(gray)
    cv2.imshow("original",img)
    cv2.imshow("gray", gray)
    cv2.imshow("dilation", dilation)
    cv2.waitKey(0)
    # 查找車牌區域
    region = findPlateNumberRegion(dilation)
    # 默認取第一個
    box = region[0]
    #畫出輪廓
    #cv2.drawContours(img, [box], 0, (0, 255, 0), 2)
    # 找出四個角的x與y點並排序
    ys = [box[0, 1], box[1, 1], box[2, 1], box[3, 1]]
    xs = [box[0, 0], box[1, 0], box[2, 0], box[3, 0]]
    ys_sorted_index = np.argsort(ys)
    xs_sorted_index = np.argsort(xs)
    # 取最小的x,y 和最大的x,y 構成切割矩形對角線
    min_x = box[xs_sorted_index[0], 0]
    max_x = box[xs_sorted_index[3], 0]
    min_y = box[ys_sorted_index[0], 1]
    max_y = box[ys_sorted_index[3], 1]

    # 切割圖片，就是取圖片二維數組的在x,y維度上的最小minX,minY 到最大maxX,maxY區間的子數組
    img_plate = img[min_y:max_y, min_x:max_x]
    return img_plate

def cutEdge(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # 2、將灰度影象二值化
    cimg_thre = img_gray
    cv2.threshold(img_gray, binary_threshold, 255, cv2.THRESH_BINARY_INV, cimg_thre)
    # 3、儲存黑白圖片
    cv2.imwrite('pic\\thre_res.png', cimg_thre)
    # 4、分割字元
    hwhite = []  # 記錄每一列的白色畫素總和
    hblack = []  # .............黑色.......
    height = cimg_thre.shape[0]
    width = cimg_thre.shape[1]
    # print(width, height)
    hwhite_max = 0
    hblack_max = 0
    # 計算每一列的黑白色畫素總和
    for i in range(height):
        hw_count = 0  # 這一列白色總數
        hb_count = 0  # 這一列黑色總數
        for j in range(width):
            if cimg_thre[i][j] == 255:
                hw_count += 1
            else:
                hb_count += 1
        hwhite_max = max(hwhite_max, hw_count)
        hblack_max = max(hblack_max, hb_count)
        hwhite.append(hw_count)
        hblack.append(hb_count)

    #print('black:',hblack)
    #print('white:',hwhite)

    #########################################
    # 切割上下白邊
    hbcount = []  # 黑點佔整列的比例

    for i in range(0, height):
        hbcount.append(hblack[i] / width)
    # print('b/(b+w):',bcount)
    # 如果黑點比例小於0.9大於0.2 記錄此列

    hstart = 0
    cu = 0
    for i in range(0, height):

        if (hbcount[i] < 0.9 and hbcount[i] > 0.2):
            cu += 1
        #print('i,h,c,c/h:', i, hbcount[i], cu, cu / height)

        if ((cu / height) < 0.5 and hbcount[i] > 0.9):
            cu = 0
        elif (cu / height) > 0.5:
            #print('ok')
            hstart = i - cu
            break
    #print(hstart)
    img = img[hstart:height, :]  # 將紀錄的那列到最後一列剪下
    cimg_thre = cimg_thre[hstart:height, :]

    height = img.shape[0]
    # 如果黑點比例大於0.9 記錄此列

    hend = 0
    cd = 0
    for i in range(height-1,-1,-1):

        if (hbcount[i+hstart] < 0.9 and hbcount[i+hstart] > 0.2):
            cd += 1
        #print('i,h,c,c/h:', i, hbcount[i], cd, cd / height)

        if ((cd / height) < 0.5 and hbcount[i] > 0.9):
            cd = 0
        elif (cd / height) > 0.5:
            #print('ok')
            hend = i + cd
            break

    img = img[0:hend, :]  # 將第一列到紀錄的那列剪下
    cimg_thre = cimg_thre[0:hend, :]
    cv2.imshow('updown', cimg_thre)
####################################################################

    vwhite = []  # 記錄每一行的白色畫素總和
    vblack = []  # .............黑色.......
    height = img.shape[0]
    width = img.shape[1]
    #print(width, height)
    vwhite_max = 0
    vblack_max = 0
    # 計算每一行的黑白色畫素總和
    for i in range(width):
        vw_count = 0  # 這一行白色總數
        vb_count = 0  # 這一行黑色總數
        for j in range(height):
            if cimg_thre[j][i] == 255:
                vw_count += 1
            else:
                vb_count += 1
        vwhite_max = max(vwhite_max, vw_count)
        vblack_max = max(vblack_max, vb_count)
        vwhite.append(vw_count)
        vblack.append(vb_count)

    #print('black:', vblack)
    #print('white:', vwhite)

    # 切割左右白邊
    vbcount = []  # 黑點佔整列的比例

    for i in range(0, width):
        vbcount.append(vblack[i] / height)
    #print('b/(b+w):', vbcount)

    # 如果黑點比例小於0.9大於0.2 記錄此列
    cl = 0
    vstart = 0
    for i in range(0, width):

        if (vbcount[i] < 0.95 and vbcount[i] > 0):
            cl += 1
        #print('i,v,c,c/w:', i, vbcount[i], cl, cl/width)
        if ((cl / width) < 0.08 and vbcount[i] > 0.95):
            cl = 0
        elif ((cl / width) > 0.08) and vbcount[i] > 0.95:
            #print('ok')
            vstart = i - cl
            break

    #print('vstart', vstart)
    img = img[:, vstart:width]  # 將紀錄的那列到最後一列剪下
    cimg_thre = cimg_thre[:, vstart:width]
    width = img.shape[1]
    #print('width:', width)
    # 如果黑點比例大於0.9 記錄此列

    cr = 0
    vend = 0
    for j in range(width - 1, -1, -1):

        if (vbcount[j + vstart] < 0.95 and vbcount[j + vstart] > 0):
            cr += 1
        #print('j,v,c,c/w:', j, vbcount[j + vstart], cr, cr / width)
        if ((cr / width) < 0.08 and vbcount[j + vstart] > 0.95):
            cr = 0
        elif ((cr / width) > 0.08) and vbcount[j + vstart] > 0.95:
            #print('ok')
            vend = j + cr
            break
    img = img[:, 0:vend+3]  # 將第一列到紀錄的那列剪下
    cimg_thre = cimg_thre[:, 0:vend+3]
    cv2.imwrite("pic\\plated.png", img)
    cv2.namedWindow('leftright', 0)
    cv2.imshow('leftright', cimg_thre)
    return img

if __name__ == '__main__':
    #車牌定位
    imageInPath = 'car4' # 图片路径
    img = cv2.imread('pic\\'+imageInPath+'.jpg')
    img = detect(img)
    cv2.imshow("img",img)
    cv2.imwrite('pic\\plate.png', img)
    img = cutEdge(img)
    imageOutPath = 'pic\\plated.png'
    cv2.imwrite(imageOutPath,img) #輸出車牌圖片
    cv2.waitKey(0)


    #字元分割
   #plate = cv2.imread('pic\\plate.png') #測試用車牌圖片
    # 1、把影象轉換為灰度影象
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # 2、將灰度影象二值化
    img_thre = img_gray
    cv2.threshold(img_gray, binary_threshold, 255, cv2.THRESH_BINARY_INV, img_thre)
    # 3、儲存黑白圖片
    cv2.imwrite('pic\\thre_res.png', img_thre)
    # 4、分割字元
    white = []  # 記錄每一列的白色畫素總和
    black = []  # .............黑色.......
    height = img_thre.shape[0]
    width = img_thre.shape[1]
    print('width,height',width, height)
    white_max = 0
    black_max = 0
    # 計算每一列的黑白色畫素總和
    for i in range(width):
        w_count = 0  # 這一列白色總數
        b_count = 0  # 這一列黑色總數
        for j in range(height):
            if img_thre[j][i] == 255:
                w_count += 1
            else:
                b_count += 1
        white_max = max(white_max, w_count)
        black_max = max(black_max, b_count)
        white.append(w_count)
        black.append(b_count)

    arg = black_max > white_max  # False表示白底黑字；True表示黑底白字
    print('w:',white)
    print('b:',black)
    print('w,bmax',white_max,black_max)

    # 分割影象
    def find_end(start_):
        end_ = start_ + 1
        for m in range(start_ + 1, width - 1):
            if (black[m] if arg else white[m]) > (
                    segmentation_spacing * black_max if arg else segmentation_spacing * white_max):
                end_ = m
                break
        return end_


    ap = 1 #切割
    n = 1
    start = 1
    end = 2
    while n < width - 1:
        n += 1
        ap += 1
        if (white[n] if arg else black[n]) > (
                (1 - segmentation_spacing) * white_max if arg else (1 - segmentation_spacing) * black_max):
            # 上面這些判斷用來辨別是白底黑字還是黑底白字
            start = n
            end = find_end(start)
            n = end
            if end - start > 5:
                print(start, end)
                cj = img_thre[1:height, start:end]
                cv2.imshow('cutChar', cj)
                cv2.waitKey(0)
                path = '../pic/cut\\'
                cv2.imwrite(str(path)+ str(imageInPath) + '_' +str(ap) + '.png', cj)