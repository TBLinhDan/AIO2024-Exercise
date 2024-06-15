''' CÂU HỎI TỰ LUẬN
Cho một list các số nguyên num_list và một sliding window có kích thước size k di
chuyển từ trái sang phải. Mỗi lần dịch chuyển 1 vị trí sang phải có thể nhìn thấy
đươc k số trong num_list và tìm số lớn nhất trong k số này sau mỗi lần trượt k phải
lớn hơn hoặc bằng 1
Input: num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1] với k=3
Output: [5, 5, 5, 5, 10, 12, 33, 33]

'''

def sliding_windown(num_list):
    output = []
    for i in range(len(num_list)-2):
        output.append(max(num_list[i:i+3]))
    return (output)


num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
print(sliding_windown(num_list))

'''
Viết function trả về một dictionary đếm số lượng chữ xuất hiện trong một từ, với key là chữ cái
và value là số lần xuất hiện
• Input: một từ
• Output: dictionary đếm số lần các chữ xuất hiện
• Note: Giả sử các từ nhập vào đều có các chữ cái thuộc [a-z] hoặc [A-Z]
'''

def char_counter(string):
    char_count_dic = {}
    for character in string:
        if character not in char_count_dic:
            char_count_dic[character] = 0
        char_count_dic[character] += 1
    return char_count_dic


string = 'smiles'
print(char_counter(string))

'''
Viết function đọc các câu trong một file txt, đếm số lượng các từ xuất hiện và trả về một dictionary
với key là từ và value là số lần từ đó xuất hiện.
• Input: Đường dẫn đến file txt
• Output: dictionary đếm số lần các từ xuất hiện
'''

def read_file(file_path):
    with open(file_path, 'r', encoding='UTF-8') as f:
        content = f.read()
        lst_word = content.split()
    return (lst_word)


def word_counter(lst):
    word_count_dic = {}
    for word in lst:
        if word not in word_count_dic:
            word_count_dic[word] = 0
        word_count_dic[word] += 1
    return (word_count_dic)


file_path = 'D:/AIO/AIO2024/Exercise/Week2/Week2/data.txt'
lst_word = read_file(file_path)
print(lst_word)
print(word_counter(lst_word))

# II. CÂU HỎI TRẮC NGHIỆM

# Câu hỏi 1: A


def max_kernel(num_list, k):
    result = []
    for i in range(len(num_list)-(k-1)):
        result.append(max(num_list[i:i+k]))
    return result


assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_kernel(num_list, k))

# a) [5, 5, 5, 5, 10, 12, 33, 33]

# Câu hỏi 2: A


def char_counter(string):
    char_count_dic = {}
    for character in string:
        if character not in char_count_dic:
            char_count_dic[character] = 0
        char_count_dic[character] += 1
    return char_count_dic


assert char_counter("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
print(char_counter('smiles'))
# a) ’s’: 2, ’m’: 1, ’i’: 1, ’l’: 1, ’e’: 1


# Câu hỏi 3: C
def read_file(file_path):
    with open(file_path, 'r', encoding='UTF-8') as f:
        content = f.read()
        lst_word = content.split()
    return (lst_word)


def word_counter(lst):
    word_count_dic = {}
    for word in lst:
        if word not in word_count_dic:
            word_count_dic[word] = 0
        word_count_dic[word] += 1
    return (word_count_dic)


file_path = 'D:/AIO/AIO2024/Exercise/Week2/Week2/data.txt'
lst_word = read_file(file_path)
result = word_counter(lst_word)
assert result['who'] == 3
print(result['man'])
# c) 6

# Câu hỏi 4: C


def levenshtein_distance(source, target):
    m = len(source)
    n = len(target)
    # Create a matrix to store the distances between prefixes.
    matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m+1):
        print(matrix[i], "")

    # Initialize the first row and column of the matrix.
    for i in range(m + 1):
        matrix[i][0] = i
    for j in range(n + 1):
        matrix[0][j] = j
    for i in range(m+1):
        print(matrix[i], "")

    # Fill in the rest of the matrix.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if source[i - 1] == target[j - 1]:
                cost = 0
            else:
                cost = 1
            matrix[i][j] = min(matrix[i - 1][j] + 1,  # deletion
                               matrix[i][j - 1] + 1,  # insertion
                               matrix[i - 1][j - 1] + cost  # substitution
                               )
    for i in range(m+1):
        print(matrix[i], "")

    # Return the distance between the last prefixes.
    distance = matrix[m][n]
    return distance

source = "hola"
target = "hello"
print(
    f"Levenshtein distance between '{source}' and '{target}' is {levenshtein_distance(source, target)}")

# levenshtein_distance("hi", " hello ") == 4.0
# Levenshtein distance between 'hola' and 'hello' is 3


# Câu hỏi 5: A

def check_the_number(num):
    list_of_numbers = []
    results = ""
    for i in range(1, 5):
        list_of_numbers.append(i)

    if num in list_of_numbers:
        results = "True"
    if num not in list_of_numbers:
        results = "False"
    return results


N = 7
assert check_the_number(N) == "False"
N = 2
results = check_the_number(N)
print(results)
# a) True

# Câu hỏi 6: C


def my_function(data, max, min):
    result = []
    for i in data:
        # Neu i < min thi them min vao result
        if i < min:
            result.append(min)
        elif i > max:
            result.append(max)
        else:
            result.append(i)
    return result


my_list = [5, 2, 5, 0, 1]
max = 1
min = 0
assert my_function(max=max, min=min, data=my_list) == [1, 1, 1, 0, 1]
my_list = [10, 2, 5, 0, 1]
max = 2
min = 1
print(my_function(max=max, min=min, data=my_list))
# c) [2, 2, 2, 1, 1]


# Câu hỏi 7: C
def my_function(x, y):
    x.extend(y)
    return x


list_num1 = ['a', 2, 5]
list_num2 = [1, 1]
list_num3 = [0, 0]
assert my_function(list_num1, my_function(list_num2, list_num3)) == [
    'a', 2, 5, 1, 1, 0, 0]

list_num1 = [1, 2]
list_num2 = [3, 4]
list_num3 = [0, 0]
print(my_function(list_num1, my_function(list_num2, list_num3)))
# c) [[1, 2, 3, 4, 0, 0]]


# Câu hỏi 8: C
#  tìm phần tử có giá trị nhỏ nhất trong một list
def my_function(n):
    return min(n)


my_list = [1, 22, 93, -100]
assert my_function(my_list) == -100

my_list = [1, 2, 3, -1]
print(my_function(my_list))
# c) -1


# Câu hỏi 9: D
#  tìm phần tử có giá trị lớn nhất trong một list
def my_function(n):
    return max(n)


my_list = [1001, 9, 100, 0]
assert my_function(my_list) == 1001

my_list = [1, 9, 9, 0]
print(my_function(my_list))
# d) 9

# Câu hỏi 10: C
# Kiểm tra number có trong intergers hay không?


def my_function(integers, number=1):
    if number in integers:
        return True
    else:
        return False


my_list = [1, 3, 9, 4]
assert my_function(my_list, -1) == False

my_list = [1, 2, 3, 4]
print(my_function(my_list, 2))
# c) True


# Câu hỏi 11: A
def my_function(list_nums=[0, 1, 2]):
    var = 0
    for i in list_nums:
        var += i
    return var/len(list_nums)


assert my_function([4, 6, 8]) == 6
print(my_function())
# a) 1.0


# Câu hỏi 12: A
def my_function(data):
    var = []
    for i in data:
        if i % 3 == 0:
            var.append(i)
    return var


assert my_function([3, 9, 4, 5]) == [3, 9]
print(my_function([1, 2, 3, 5, 6]))
# a) [3, 6]


# Câu hỏi 13: C
def my_function(y):
    var = 1
    i = 1
    while (i <= y):
        var *= i
        i += 1
    return var


assert my_function(8) == 40320
print(my_function(0))
# c) 24


# Câu hỏi 14: B
def my_function(x):
    return x[::-1]


x = 'I can do it'
assert my_function(x) == "ti od nac I"

x = 'apricot'
print(my_function(x))
# b) tocirpa


# Câu hỏi  15: C
def function_helper(x):
    if x > 0:
        return 'T'
    else:
        return 'N'


def my_function(data):
    res = [function_helper(x) for x in data]
    return res


data = [10, 0, -10, -1]
assert my_function(data) == ['T', 'N', 'N', 'N']

data = [2, 3, 5, -1]
print(my_function(data))
# c) [’T’, ’T’, ’T’, ’N’


# Câu hỏi 16: A
# loại bỏ những phần tử trùng nhau

def remove_dupplicate_number(data):
    filter_lst = []
    for element in data:
        if element not in filter_lst:
            filter_lst.append(element)
    return filter_lst


lst = [10, 10, 9, 7, 7]
assert remove_dupplicate_number(lst) == [10, 9, 7]

lst = [9, 9, 8, 1, 1]
print(remove_dupplicate_number(lst))

# [9, 8, 1]
