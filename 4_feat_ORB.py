import cv2

img = cv2.imread("image.jpg")
resize_image = cv2.resize(img, dsize=(1280, 720))

#ORB特徴点抽出
#detector = cv2.ORB_create()
#KAZE特徴量抽出
#detector = cv2.KAZE_create()
#SIFT特徴量抽出
detector = cv2.SIFT_create()

#特徴抽出
keypoints = detector.detect(resize_image)

#特徴点を画像へ書き込む
img_orb = cv2.drawKeypoints(resize_image, keypoints, None)

#画像の表示
cv2.imshow("ORB_Image", img_orb)
cv2.waitKey()


#https://qiita.com/taka_baya/items/453e429b466ffaa702c9
#https://python-debut.blogspot.com/2020/02/blog-post_24.html