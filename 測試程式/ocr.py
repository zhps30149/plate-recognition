from PIL import Image
import pytesseract

def main():
    pytesseract.pytesseract.tesseract_cmd = r'E:\code\plate analyze\Tesseract-OCR\tesseract.exe'
    #指定tesseract.exe執行檔位置
    img = Image.open('/pic/platetest.jpg') #圖片檔案位置
    text = pytesseract.image_to_string(img, lang='eng', config='--psm 7') #讀英文
    print(text)


if __name__ == '__main__':
    main()