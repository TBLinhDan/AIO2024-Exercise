import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread('dog.jpeg')
plt.imshow(img)
plt.show()

# chuyển ảnh màu sang ảnh xám dựa vào phương pháp Lightness:
# Lightness: Tính giá trị trung bình của giá trị lớn nhất và nhỏ nhất cho các kênh màu: (max(R,G,B)+ min(R,G,B))/2  --> return (np.max(vector) + np.min(vector))/2

def compute_averate(vector):
    return np.max(vector)*0.5 + np.min(vector)*0.5

gray_img_01 = np.apply_along_axis(compute_averate, axis = 2, arr = img)

plt.imshow(gray_img_01, cmap=plt.get_cmap('gray'))
plt.show()
print(gray_img_01.shape)
print(gray_img_01)
print(gray_img_01[0,0])

# chuyển ảnh màu sang ảnh xám dựa vào phương pháp Average:
# Average: Tính giá trị trung bình của 3 kênh màu: (R+G+B)/3 --> return np.sum(vector)/3

def compute_averate(vector):
    return vector[0]*1/3 + vector[1]*1/3 + vector[2]*1/3

gray_img_02 = np.apply_along_axis(compute_averate, axis = 2, arr = img)

plt.imshow(gray_img_02, cmap=plt.get_cmap('gray'))
plt.show()
print(gray_img_02.shape)
print(gray_img_02)
print(gray_img_02[0,0])

# chuyển ảnh màu sang ảnh xám dựa vào phương pháp Luminosity:
# Luminosity: Nhân hệ số tương ứng của 3 kênh màu như sau: 0.21*R + 0.72*G + 0.07*B

def compute_averate(vector):
    return vector[0]*0.21 + vector[1]*0.72 + vector[2]*0.07

gray_img_03 = np.apply_along_axis(compute_averate, axis = 2, arr = img)

plt.imshow(gray_img_03, cmap=plt.get_cmap('gray'))
plt.show()
print(gray_img_03.shape)
print(gray_img_03)
print(gray_img_03[0,0])

