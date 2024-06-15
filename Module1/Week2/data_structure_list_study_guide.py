''' Section 1
• Câu 1: Tạo mới 1 List gồm các số từ 1 đến 10.
• Câu 2: In ra kết quả 5 phần tử đầu tiên có trong List trên
• Câu 3: In ra kết quả phần tử có giá trị không chia hết cho 2 (dùng kết hợp với vòng lặp for)
• Câu 4: In ra kết quả tổng các giá trị trong list (dùng kết hợp với vòng lặp for)
'''
import math
lst_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("The first 5 elements in data_List:")
the_first_5_elements = []
for i in range(5):
    the_first_5_elements.append(i)
print(the_first_5_elements)

print("\nThe number is not divisible by 2 in data_List:")
number_is_not_divisible_by_2 = []
for i in range(10):
    if lst_data[i] % 2 != 0:
        number_is_not_divisible_by_2.append(lst_data[i])
print(number_is_not_divisible_by_2)

print("\nSum of elements in data_List:")
sum = 0
for i in range(10):
    sum += lst_data[i]
print(sum)

''' Section 2
• Câu 1: Tạo mới một List có tên là lst_data, gồm các số chẵn từ 1 đến 12.
• Câu 2: Xóa tất cả các số chia hết cho 3 trong lst_data vừa tạo
• Câu 3: Thêm vào cuối lst_data các số từ 1 đến 3, và thêm vào vị trí index = 3 một chuỗi các số từ 6 đến 8
• Câu 4: Nếu các số trong list lst_data chia hết cho 2 hoặc chia hết cho 5 thì cập nhật thành số 0
'''
lst_data = [2, 4, 6, 8, 10, 12]
print(lst_data)

for i in range(len(lst_data)):
    if lst_data[i] % 3 == 0:
        print(i, lst_data[i])
        # lst_data.pop(i)
lst_data.pop(2)
lst_data.pop(4)
print(lst_data)

for i in range(1, 4):
    lst_data.append(i)
print(lst_data)

for i in range(3, 6):
    lst_data.insert(i, i+3)
print(lst_data)

for i in range(len(lst_data)):
    if lst_data[i] % 2 == 0 or lst_data[i] % 5 == 0:
        lst_data[i] = 0
        # print(lst_data[i])
print(lst_data)

''' Section 3
• Bước 1: Viết hàm xét số Armstrong, hàm trả về 1 nếu phần tử đang xét là số
Armstrong, ngược lại trả về 0.
• Bước 2: Chạy vòng lặp qua tất cả các phần tử của list.
• Bước 3: Xét điều kiện nếu phần từ là số Armtrong thì lưu vào 1 list khác.
• Bước 4: In ra list kết quả chứa các số Armstrong đã xét.
'''
test_case_1 = [130, 270, 153, 407, 177, 371, 1000, 1634, 370]
result = []


def cal_armstrong(number):
    def convert_decimal_numbers(number):
        d = len(str(number))
        number = str(number)
        sum_number = 0
        for i in range(d):
            sum_number += (int(number[i])**d)
        return (sum_number)
    if number == convert_decimal_numbers(number):
        return 1
    else:
        return 0


for i in range(len(test_case_1)):
    if cal_armstrong(test_case_1[i]) == 1:
        result.append(test_case_1[i])
print(f'The Armstrong numbers included in the list are:\n {result}')


''' Section 4
'''

def test_case():
    candies = [12, 1, 12]
    resull = []
    extra_candies = 10
    min_value = 0
    i = 0
    while i <= (len(candies) - 2):
        if candies[i] + extra_candies <= candies[i+1] + extra_candies:
            min_value = candies[i] + extra_candies
        i += 1

    for i in range(len(candies)):
        if candies[i] + extra_candies > min_value:
            resull.append(True)
        else:
            resull.append(False)
    return (resull)


print(test_case())

''' Section 5 - Computing MEDIAN for a list of numbers
• Câu 1: Tạo mới một List có tên là lst_data, gồm các số từ 1 đến 10.
• Câu 2: Tính giá trị trung vị từ lst_data vừa tạo. (Không sử dụng numpy)
• Câu 3: Lọc các giá trị số lẻ trong lst_data và lưu ra list mới có tên là: lst_odd_f ilter
với thứ tự giảm dần ( Sử dụng phương thức reverse=True trong hàm sort/sorted).
'''

lst_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

N = int(len(lst_data))
median = 0
if N % 2 == 0:
    median = (lst_data[int(N/2)] + lst_data[int(N/2 - 1)])/2
else:
    median = lst_data[int((N-1)/2)]

print(lst_data)
print("Median: ", median)

lst_odd_filter = []
for i in range(len(lst_data)):
    if lst_data[i] % 2 != 0:
        lst_odd_filter.append(lst_data[i])

print(lst_odd_filter)
lst_odd_filter.sort(reverse=True)
print(f"Sắp xếp theo thứ tự giảm dần:\n {lst_odd_filter}")


'''Section 6 - Computing MEAN for a list of numbers
• Câu 1: Tạo mới một List có tên là lst_data, gồm các số từ 1 đến 10.
• Câu 2: Tính giá trị trung bình cho các số lẻ và số chẵn từ lst_data vừa tạo.
(Không sử dụng numpy)
• Câu 3: Tính giá trị trung bình và trung vị cho tất cả dữ liệu trong lst_data
và cho nhận xét.

'''
lst_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count_even = 0
count_odd = 0
sum_even = 0
sum_odd = 0
mean_even = 0
mean_odd = 0
mean = 0
for i in range(len(lst_data)):
    if lst_data[i] % 2 == 0:
        count_even += 1
        sum_even += lst_data[i]
        mean_even = sum_even / count_even
    else:
        count_odd += 1
        sum_odd += lst_data[i]
        mean_odd = sum_odd / count_odd
    mean = (sum_even + sum_odd) / (count_even + count_odd)

print(f"Mean_even: {mean_even}")
print(f"Mean_odd: {mean_odd}")
print(f"Mean: {mean}")


'''Section 7 - Bag of Words (NLP)
Tạo Bag-Of-Word cho tập dataset sau: corpus = ["Tôi thích môn Toán",
"Tôi thích AI", "Tôi thích âm nhạc"]. Sau đó tạo list có tên vector để lưu vector sau
khi thực hiện bước Tokenization đoạn văn bản sau: Tôi thích AI thích Toán, biết
Bag-Of-Word được sắp theo thứ tự tăng dần
'''
vocabulary = []
corpus = ["Tôi thích môn Toán", "Tôi thích AI", "Tôi thích âm nhạc"]
print("Dataset:\n")
for i in range(len(corpus)):
    print(corpus[i])
    for j in range(len(corpus[i].split())):
        # print(corpus[i].split()[j])
        if corpus[i].split()[j] not in vocabulary:
            vocabulary.append(corpus[i].split()[j])

vocabulary.sort(reverse=False)
print(f"\nBag-of-Words: {vocabulary}")

zero_list = [0] * len(vocabulary)
# print(zero_list)
i = 0
str = "Tôi thích AI thích Toán"
# print(str.split())
for i in range(len(vocabulary)):
    for j in range(len(str.split())):
        if vocabulary[i] == str.split()[j]:
            zero_list[i] += 1

print(f"{str}: {zero_list}")

'''Section 8 - Algorithms on List
 Tạo List có tên là lst_data = [1, 1.1, None, 1.4, None, 1.5, None, 2.0]. Sau đó, áp
dụng phương pháp tìm kiếm để tìm vị trí có giá trị None có trong lst_data theo
2 cách: tìm vị trí None đầu tiên, và tìm tất cả vị trí có giá trị None
'''
lst_data = [1, 1.1, None, 1.4, None, 1.5, None, 2.0]
none_location = []
for i in range(len(lst_data)):
    if lst_data[i] is None:
        none_location.append(i)

print(f"Vị trí None đầu tiên: {none_location[0]}")
print(f"Danh sách vị trí có giá trị None: {none_location}")


''' Section 9 - Interpolation for List (Time-series)
 Tạo List có tên là lst_data = [1, 1.1, None, 1.4, None, 1.5, None, 2.0]. Sau đó,
áp dụng phương pháp nội suy Nearest Neighbor để gắn giá trị None có trong
lst_data
'''
lst_data = [1, 1.1, None, 1.4, None, 1.5, None, 2.0]

for i in range(len(lst_data)):
    if lst_data[i] is None:
        if i == 0:
            lst_data[i] = lst_data[i+1]
        else:
            lst_data[i] = lst_data[i-1]
print(lst_data)

''' Section 10 - 2D List
 Tạo List 2D có tên là lst_data có dạng 3 x 3, gồm các số từ 1 đến 9, ứng với các
vị trí trong List. Sau đó tạo list khác có tên lst_sub_data là 2D List để lưu giá
trị tại vị trí index thứ 0 và thứ 2 của lst_data (Chỉ sử dụng For). In ra màn hình
kết quả của lst_sub_data

'''
lst_data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

lst_sub_data = [[0, 0] for _ in range(len(lst_data))]

for i in range(len(lst_data)):
    lst_sub_data[i][0] = lst_data[i][0]
    lst_sub_data[i][1] = lst_data[i][2]

print(lst_sub_data)

''' Section 11 - Matrix representation using List
Câu 1. Hãy tính tổng và hiệu 2 ma trận A + B và A - B
Câu 2. Hãy tính dot product 2 ma trận A và B
'''
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

b = [[2, 4, 6],
     [1, 3, 5],
     [1, 0, 1]]

result_c_add = [[0, 0, 0] for _ in range(len(a))]
result_c_sub = [[0, 0, 0] for _ in range(len(a))]
result_c_multi = [[0, 0, 0] for _ in range(len(a))]


def matrix_addition(a, b):
    for i in range(len(a)):
        for j in range(len(b)):
            result_c_add[i][j] = a[i][j] + b[i][j]

    return (result_c_add)


result_add_matrix = matrix_addition(a, b)
print(f"Matrix addition:\n {result_add_matrix}")


def matrix_subtraction(a, b):
    for i in range(len(a)):
        for j in range(len(b)):
            result_c_sub[i][j] = a[i][j] - b[i][j]

    return (result_c_sub)


result_sub_matrix = matrix_subtraction(a, b)
print(f"Matrix Subtraction:\n {result_sub_matrix}")


def matrix_multiplication(a, b):

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result_c_multi[i][j] += a[i][k] * b[k][j]
    return (result_c_multi)


result_multi_matrix = matrix_multiplication(a, b)
print(f"Dot Product:\n {result_multi_matrix}")

''' Section 12 - List Comprehension
Hãy loại bỏ các từ có trong stop_words
= ["I", "love", "and", "to"] câu đầu vào "I love AI and listen to music". Hãy áp
dụng List comprehension và For truyền thống để thực hiện
'''
stop_words = ["I", "love", "and", "to"]
sentence = "I love AI and listen to music"

filter_lst = []
split_lst = sentence.split()
for i in range(len(split_lst)):
    if split_lst[i] not in stop_words:
        filter_lst.append(split_lst[i])
print(filter_lst)

# using List comprehension

filter_lst = [word for word in split_lst if word not in stop_words]
print(filter_lst)

'''Section 13 - List and Tuple
• Câu 1: Tạo mới hai Tuple: my_tuple1 = (2,3), my_tuple2 = (3,6) mỗi Tuple có
2 phần tử đại diện cho một vector trong không gian 2D.
• Câu 2: In ra kết quả của tổng và tích 2 vector trên.
• Câu 3: In ra kết quả của khoảng cách của hai vector trên theo công thức.
• Câu 4: In ra vị trí của phần tử có giá trị là 3
Sử dụng cú pháp: my_tuple.index(values) để trích xuất vị trí của giá trị cần tìm.'''

# Tupple
my_tuple1 = (2, 3)
my_tuple2 = (3, 6)
# tổng và tích 2 vector
sum_vector1 = tuple([i+j for i, j in zip(my_tuple1, my_tuple2)])
multil_vector2 = tuple([i*j for i, j in zip(my_tuple1, my_tuple2)])
print(f"sum_vector1 ={sum_vector1}, multil_vector2={multil_vector2}")

# khoảng cách của 2 vector
distance = math.sqrt(sum([(i-j)**2 for i, j in zip(my_tuple1, my_tuple2)]))
print(distance)

# vị trí của phần tử có giá trị là 3
value = 3
index = (my_tuple1.index(value), my_tuple2.index(value))
print(index)
