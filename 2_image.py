import cv2
from cv2 import threshold

#画像の読み込み
img = cv2.imread("image.jpg")

#表示
cv2.imshow("Image", img)
#キー入力待ち(これがないとすぐ閉じちゃう?)
cv2.waitKey()


#縮小(解像度指定)
resize_image = cv2.resize(img, dsize=(1280, 720))
cv2.imshow("Resize_Image", resize_image)
cv2.waitKey()

#拡大(倍率指定)
resize_image2 = cv2.resize(img, dsize=None, fx=2, fy=2)
cv2.imshow("Resize_Image2", resize_image2)
cv2.waitKey()

#回転
Rotate_image = cv2.rotate(resize_image, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Rotate_Image", Rotate_image)
cv2.waitKey()



#画像の読み込み（グレースケール）
img2 = cv2.imread("image2.jpg", 0)
#しきい値の設定と2値化
threshold = 100
ret, img_thresh = cv2.threshold(img2, threshold, 255, cv2.THRESH_BINARY)
#画像の表示
cv2.imshow("Binary_Image", img_thresh)
cv2.waitKey()

#しきい値を自動で決定する
ret2, img_otsu = cv2.threshold(img2, 0, 255, cv2.THRESH_OTSU)
print("ret2: {}".format(ret2))
#画像の表示
cv2.imshow("Binary_Image2", img_otsu)
cv2.waitKey()

#全部消す
cv2.destroyAllWindows()

"""保存用"""
"""
cv2.imwrite("Img_Res.jpg", resize_image)
cv2.imwrite("Img_Rote.jpg", Rotate_image)
cv2.imwrite("Img_Bin1.jpg", img_thresh)
cv2.imwrite("Img_Bin2.jpg", img_otsu)
"""

#https://imagingsolution.net/program/python/opencv-python/imread_imshow/#:~:text=OpenCV%E3%81%A7Bmp%E3%82%84Jpeg,%E3%82%8C%E3%81%9F%E3%82%BF%E3%82%A4%E3%83%9F%E3%83%B3%E3%82%B0%E3%81%A8%E3%81%AA%E3%82%8A%E3%81%BE%E3%81%99%E3%80%82
#https://pystyle.info/opencv-resize/
#https://qiita.com/tokkuri/items/ad5e858cbff8159829e9