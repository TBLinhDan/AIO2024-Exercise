'''
Viết class và cài phương thức softmax.
Trong pytorch, torch.nn.Module là lớp cơ bản để từ đó xây dựng lên các mô hình hoặc các phương
thức kích hoạt (activation funtion) như sigmoid, softmax,... Trong phần này, chúng ta xây dựng
class Softmax và softmax_stable nhận đầu vào là mảng 1 chiều (tensor 1 chiều) dựa vào kế thừa
từ lớp Module và ghi đè vào phương thức forward()
'''
import torch
import torch.nn as nn

class MySoftmaxActivation(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        return x_exp / torch.sum(x_exp)

class softmaxstable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x) :
        x_max = torch.max(x)
        x_exp = torch.exp(x - x_max)
        return x_exp / torch.sum(x_exp)

data = torch.Tensor([1, 2, 3])
my_softmax = MySoftmaxActivation()
out_softmax = my_softmax(data)
print(out_softmax)

softmax_stable = softmaxstable()
out_softmax_stable = softmax_stable(data)
print(out_softmax_stable)

