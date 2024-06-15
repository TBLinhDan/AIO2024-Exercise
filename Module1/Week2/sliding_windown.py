'''Cho một list các số nguyên num_list và một sliding window có kích thước size k di
chuyển từ trái sang phải. Mỗi lần dịch chuyển 1 vị trí sang phải có thể nhìn thấy
đươc k số trong num_list và tìm số lớn nhất trong k số này sau mỗi lần trượt k phải
lớn hơn hoặc bằng 1
Input: num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1] với k=3
Output: [5, 5, 5, 5, 10, 12, 33, 33]
'''

def max_kernel(num_list, k):
    output = []
    for i in range(len(num_list)-(k-1)):
        output.append(max(num_list[i:i+k]))
    return (output)

assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
check_list = [3, 4, 5, 1, -44]
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]

print("sliding window finds the largest number of size 3 moving from left to right in the list:")
print(f"{check_list}: {max_kernel([3, 4, 5, 1, -44], 3)}")
print(f"{num_list}: {max_kernel(num_list, 3)}")

print("\nsliding window finds the largest number of size 5 moving from left to right in the list:")
print(f"{num_list}: {max_kernel(num_list, 5)}")

'''
sliding window finds the largest number of size 3 moving from left to right in the list:
[3, 4, 5, 1, -44]:                      [5, 5, 5]
[3, 4, 5, 1, -44, 5, 10, 12, 33, 1]:    [5, 5, 5, 5, 10, 12, 33, 33]

sliding window finds the largest number of size 5 moving from left to right in the list:
[3, 4, 5, 1, -44, 5, 10, 12, 33, 1]:    [5, 5, 10, 12, 33, 33]
'''



