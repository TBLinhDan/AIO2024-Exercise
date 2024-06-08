#1. classification model

def calc_f1_score(tp, fp, fn):
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)
    return(f1_score)

def exercise1(tp, fp, fn):
    if (type(tp) != int) or (type(fp) != int) or (type(fn) != int):
        if type(tp) != int:
            print("tp must be int")
           # return
        elif type(fp) != int:
            print("fp must be int")
            #return
        elif type(fn) != int:
            print("fn must be int")
            #return
    else:
        if (tp > 0) and (fp > 0) and (fn > 0):
            precision = tp / (tp + fp)
            recall = tp / (tp + fn)
            f1_score = 2 * (precision * recall) / (precision + recall)
            print(f"precision is : {precision}")
            print(f"recall is : {recall}")
            print(f"f1_score : {f1_score}")
        else:
            return ("tp and fp and fn must be greater than zero")
print("Input correct number")
print(exercise1(tp=2, fp=3, fn=4))
print(f"\nInput incorrect type of fp")
print(exercise1(tp=2, fp='a', fn=4))
print(f"\nInput incorrect type of fn")
print(exercise1(tp=2, fp=3, fn='a'))
print(f"\nInput fn = 0")
print(exercise1(tp=2, fp=3, fn=0))

print(f"\nmultiple-choice questions No 1")
assert round(calc_f1_score(tp =2, fp =3, fn =5), 2) == 0.33
print (round( calc_f1_score(tp =2, fp =4, fn =5), 2))

