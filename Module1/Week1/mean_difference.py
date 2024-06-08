#5. Mean Difference
import numpy as np

def calc_ae(y, y_hat):
    return np.abs(y - y_hat)

print(f"\nmultiple-choice questions No 7")
y = 1
y_hat = 6
assert calc_ae(y, y_hat) ==5
y = 2
y_hat = 9
print (calc_ae(y, y_hat))

print(f"\nmultiple-choice questions No 8")
def calc_se (y, y_hat):
    x = np.abs(y - y_hat)
    return  x ** 2

y = 4
y_hat = 2
assert calc_se(y, y_hat) == 4
print(calc_se(2, 1))

print(f"\nmultiple-choice questions No 13")
def md_nre_single_sample(y , y_hat , n , p) :
    y_root = y ** (1/n)
    y_hat_root = y_hat ** (1/n)
    difference = y_root - y_hat_root
    loss = difference ** p
    return loss

print(md_nre_single_sample(100, 99.5, 2, 1))
print(md_nre_single_sample(50, 49.5, 2, 1))
print(md_nre_single_sample(20, 19.5, 2, 1))
print(md_nre_single_sample(0.6, 0.1, 2,1))



