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
word_lst = word_counter(lst_word)
who_number, man_number, success_number = word_lst['who'], word_lst['man'], word_lst['success']
print(word_lst)
print(f'\nThe number of times the word "who" appears in the file is: {who_number}')  # 3
print(f'The number of times the word "man" appears in the file is: {man_number}')  # 6
print(f'The number of times the word "success" appears in the file is: {success_number}')
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

string_lst = ['smiles', 'success']
for string in string_lst:
    print(f'\nThe number of times the characters appear in the word "{string}" is:')
    print(char_counter(string))     # {'s': 2, 'm': 1, 'i': 1, 'l': 1, 'e': 1}

'''
The number of times the word "who" appears in the file is: 3
The number of times the word "man" appears in the file is: 6
The number of times the word "success" appears in the file is: 2

The number of times the characters appear in the word "smiles" is:
{'s': 2, 'm': 1, 'i': 1, 'l': 1, 'e': 1}

The number of times the characters appear in the word "success" is:
{'s': 3, 'u': 1, 'c': 2, 'e': 1}

'''