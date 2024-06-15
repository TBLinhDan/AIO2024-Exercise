'''
Khoảng cách Levenshtein thể hiện khoảng cách khác biệt giữa 2 chuỗi ký tự. 
Khoảng cách Levenshtein giữa chuỗi S và chuỗi T là số bước ít nhất biến chuỗi S thành chuỗi T thông qua 3 phép biến đổi là:
• Xoá một ký tự
• Thêm một ký tự
• Thay thế ký tự này bằng ký tự khác
Khoảng cách này được sử dụng trong việc tính toán sự giống và khác nhau giữa 2 chuỗi:
Ví dụ: khoảng cách cần tính giữa hai từ source: ’yu’ và target: ’you’. 
Đầu tiên ký tự ’y’ giữ nguyên sau đó thực hiện 1 phép thêm ký tự ’o’ vào sau ký tự ’y’ 
và cuối cùng ký tự ’u’ được giữ nguyên. Vì vậy khoảng cách chỉnh sửa từ source: ’yu’ sang thành target: ’you’ là 1

Chi phí thực hiện cho các phép biến đổi bao gồm: 
xoá một ký tự, thêm một ký tự và thay thế ký tự này thành ký tự khác đều là 1 
(Nếu 2 ký tự giống nhau thì chi phí thực hiện là 0).

'''
def levenshtein_distance(source, target):
    m = len(source)
    n = len(target)
    # Create a matrix to store the distances between prefixes.
    matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m+1):
        print(matrix[i],"")

    # Initialize the first row and column of the matrix.
    for i in range(m + 1):
        matrix[i][0] = i
    for j in range(n + 1):
        matrix[0][j] = j
    for i in range(m+1):
        print(matrix[i],"")

    # Fill in the rest of the matrix.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if source[i - 1] == target[j - 1]:
                cost = 0
            else:
                cost = 1
            matrix[i][j] = min( matrix[i - 1][j] + 1,  # deletion
                                matrix[i][j - 1] + 1,  # insertion
                                matrix[i - 1][j - 1] + cost  # substitution
                                )
    for i in range(m+1):
        print(matrix[i],"")

    # Return the distance between the last prefixes.
    distance = matrix[m][n]
    return distance

source = "hi"
target = "hello"
print(f"Levenshtein distance between '{source}' and '{target}' is {levenshtein_distance(source, target)}")

'''
[0, 0, 0, 0, 0, 0] 
[0, 0, 0, 0, 0, 0] 
[0, 0, 0, 0, 0, 0]

[0, 1, 2, 3, 4, 5]
[1, 0, 0, 0, 0, 0]
[2, 0, 0, 0, 0, 0]

[0, 1, 2, 3, 4, 5]
[1, 0, 1, 2, 3, 4]
[2, 1, 1, 2, 3, 4]

Levenshtein distance between 'hi' and 'hello' is 4
'''