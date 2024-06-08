#3. regression loss function

import numpy as np
import math

num_sample = input("Input number of samples:")

if num_sample.isnumeric():
    num_sample = int(num_sample)
    predict = []
    target = []
    for i in range(num_sample):
        random_number_predict = np.random.uniform(0,10)
        predict.append(random_number_predict)
    print(f"predict list:\n {predict}")

    for i in range(num_sample):
        random_number_target = np.random.uniform(0,10)
        target.append(random_number_target)
    print(f"target list:\n {target}")

    def loss_func(name):
        if name == "MAE":
            #print(f"\nloss name: MAE")
            for i in range(num_sample):
                print(f"loss name: MAE, samlpe: {i}, predict: {predict[i]}, target: {target[i]}")
                print(f"loss: {abs(predict[i] - target[i])}")
        elif name == "MSE":
            #print(f"\nloss name: MSE")
            for i in range(num_sample):
                print(f"loss name: MSE, samlpe: {i}, predict: {predict[i]}, target: {target[i]}")
                print(f"loss: {((predict[i] - target[i])) ** 2}")
        else:
            #print(f"\nloss name: RMSE")
            for i in range(num_sample):
                print(f"loss name: RMSE, samlpe: {i}, predict: {predict[i]}, target: {target[i]}")
                print(f"loss: {math.sqrt(((predict[i] - target[i])) ** 2)}")

    loss_name = input("Input loss name (MAE | MSE | RMSE) :")

    if (loss_name == "MAE") or (loss_name == "MSE") or (loss_name == "RMSE"):
        loss_func(loss_name)
    else:
        print("the name_function_user is not supported")

else:
    print("number of samples must be an integer number")

