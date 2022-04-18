import cv2

#画像を読み込む, 第2引数はカラー
img1 = cv2.imread("diff_test1.jpg", 1)
img2 = cv2.imread("diff_test2.jpg", 1)
#グレースケール
img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#画像を引き算(差分の絶対値を計算)
img_diff = cv2.absdiff(img1_gray, img2_gray)

#2値化
ret2, img_th = cv2.threshold(img_diff, 20, 255, cv2.THRESH_BINARY)

#画像を表示
cv2.imshow("DiffImage", img_th)
cv2.waitKey()


#https://torimakujoukyou.com/python-opencv-diff/
#https://daeudaeu.com/python-diff/

"""	なんで差分を絶対値とる？
	グレースケールにする理由
"""