#2. activation function
import math
import numpy as np

def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

print(f"\nmultiple-choice questions No 2")
assert is_number(3) == 1.0
assert is_number('-2a') == 0.0
print (is_number (1))
print (is_number ('n'))

def relu(x):
    if x > 0:
        return x
    else:
        return
print(f"\nmultiple-choice questions No 3")
data = [1, 5, -4, 3, -2]
for i in range(len(data)):
    print(relu(data[i]))

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

print(f"\nmultiple-choice questions No 4")
data = [1, 5, -4, 3, 4]
for i in range(len(data)):
    print(round(sigmoid(data[i]), 2))
assert round(sigmoid(3), 2) == 0.95
#print(f"\n")
print(round(sigmoid(2), 2))

def elu(x, alpha=0.01):
    if x > 0:
        return x
    else:
        return alpha * (np.exp(x) - 1)

print(f"\nmultiple-choice questions No 5")
data = [1, 5, -4, 3, -2]
for i in range(len(data)):
    print(elu((data[i]), alpha=0.01))
print(f"\n")
assert round(elu(1)) == 1
print (round(elu(-1), 2))

def calc_activation_func(x, act_name):
    if act_name == "sigmoid":
        return sigmoid(x)
    elif act_name == "relu":
        return relu(x)
    else:
        return elu(x, alpha=0.01)

print(f"\nmultiple-choice questions No 6")
assert calc_activation_func(1, "relu") == 1
print (round(calc_activation_func(3, "sigmoid"), 2))
print(f"\n")

def exercise2():
    x = input("Input x:")
    if is_number(x):
        name = input("Input activation Function (sigmoid | relu | elu) :")
        if (name == "sigmoid") or (name == "relu") or (name == "elu"):
            result = calc_activation_func(float(x), name)
            print(f"{name}: f({x}) ={result}")
        else:
            print("the name_function_user is not supported")
    else:
        print("x must be a number")

exercise2()

'''
Input x: abc
x must be a number

Input x: 1.5
Input activation Function (sigmoid | relu | elu) : bulu
the name_function_user is not supported
'''