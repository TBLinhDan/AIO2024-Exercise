'''
Thực hiện xây dựng class Queue với các chức năng (method) sau đây
• initialization method nhận một input "capacity": dùng để khởi tạo queue với capacity là số lượng element mà queue có thể chứa
• .is_empty(): kiểm tra queue có đang rỗng
• .is_full(): kiểm tra queue đã full chưa
• .dequeue(): loại bỏ first element và trả về giá trị đó
• .enqueue(value) add thêm value vào trong queue
• .front() lấy giá trị first element hiện tại của queue, nhưng không loại bỏ giá trị đó
'''

class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []
    def __str__(self):
        return f"The capacity of My Queue is = {self.__capacity}"
    
    def print(self):
        print(self.__queue)
    
    # Enqueue funtion: can not add item if queue is already full
    def is_full(self):
        if len(self.__queue) == self.__capacity:
            return True
        else:
            return False

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full, please rake out if you want to add more")
        else:
            self.__queue.append(item)

    # Dequeue funtion, can not get out item if queue is empty
    def is_empty(self):
        if len(self.__queue) == 0:
            return True
        else:
            return False

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, please add more if you want to rake out")
        else:
            return self.__queue.pop(0)

    def first_item(self):
        if not self.is_empty():
            return self.__queue[0]
        else:
            print("Queue is empty")

queue1 = MyQueue(5)
print(queue1)
queue1.enqueue(1)
is_emty = queue1.is_empty()
print(f"Is the queue empty? {is_emty}")
queue1.print()
queue1.enqueue(4)
queue1.enqueue(2)
queue1.enqueue(3)

is_full = queue1.is_full()
print(f"Is the queue already full? {is_full}")
queue1.print()
first_item = queue1.first_item()
print(f"The first item: {first_item}")
queue1.dequeue()
queue1.print()
queue1.enqueue(5)
queue1.enqueue(6)
queue1.print()
first_current_item = queue1.first_item()
print(f"The first current item: {first_current_item}")

''' Result:
The capacity of My Queue is = 5
Is the queue empty? False
[1]

Is the queue already full? False
[1, 4, 2, 3]

The first item: 1
[4, 2, 3]

[4, 2, 3, 5, 6]
The first current item: 4
'''