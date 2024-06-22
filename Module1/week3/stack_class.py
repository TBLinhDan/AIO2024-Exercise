'''
Thực hiện xây dựng class Stack với các phương thức (method) sau đây
• initialization method nhận một input "capacity": dùng để khởi tạo stack với capacity là số lượng element mà stack có thể chứa
• .is_empty(): kiểm tra stack có đang rỗng
• .is_full(): kiểm tra stack đã full chưa
• .pop(): loại bỏ top element và trả về giá trị đó
• .push(value) add thêm value vào trong stack
• .top() lấy giá trị top element hiện tại của stack, nhưng không loại bỏ giá trị đó
'''

class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []
    def __str__(self):
        return f"The capacity of My Stack is = {self.__capacity}"

    # push funtion: can not push if stack is already full
    def is_full(self):
        if len(self.__stack) == self.__capacity:
            return True
        else:
            return False

    def push(self, item):
        if self.is_full():
            print("Stack is full, please pop more if you want to push again")
        else:
            self.__stack.append(item)

    # pop funtion: can not pop if stack is empty
    def is_empty(self):
        if len(self.__stack) == 0:
            return True
        else:
            return False

    def pop(self):
        if self.is_empty():
            print("Stack is empty, please push more if you want to pop again")
        else:
            return self.__stack.pop(-1)

    def print(self):
        print(self.__stack)

    def top(self):
        if not self.is_empty():
            return self.__stack[-1]
        else:
            print("Stack is empty")


stack1 = MyStack(5)
print(stack1)
is_emty = stack1.is_empty()
print(f"Is the stack empty? {is_emty}")
stack1.print()
stack1.push(1)
stack1.push(2)
stack1.push(3)

is_full = stack1.is_full()
print(f"Is the stack already full? {is_full}")
stack1.print()
item_top = stack1.top()
print(f"Top item: {item_top}")
stack1.pop()
stack1.print()
stack1.push(5)
stack1.push(6)
stack1.print()
item_current_top = stack1.top()
print(f"Item current Top: {item_current_top}")

''' Result:
The capacity of My Stack is = 5
Is the stack empty? True
[]

Is the stack already full? False
[1, 2, 3]

Top item: 3
[1, 2]

[1, 2, 5, 6]
Item current Top: 6

'''
