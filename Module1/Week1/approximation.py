#4. approximation

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

def approx_cos(x, n):
    cos_x = 0
    for i in range(n+1):
        cos_x += ((-1)**i)*(x ** (2*i)) / factorial(2*i)
    return cos_x

print(f"\nmultiple-choice questions No 9")
assert round(approx_cos(1 , 10), 2) == 0.54
print (round(approx_cos(3.14, n =10), 2))

def approx_sin(x, n):
    sin_x = 0
    for i in range(n+1):
        sin_x += ((-1)**i)*(x ** (2*i+1)) / factorial(2*i+1)
    return sin_x

print(f"\nmultiple-choice questions No 10")
assert round(approx_sin(1, 10), 4) == 0.8415
print (round(approx_sin(3.14, 10), 4))

def approx_sinh(x, n):
    sinh_x = 0
    for i in range(n+1):
        sinh_x += (x ** (2*i+1)) / factorial(2*i+1)
    return sinh_x

print(f"\nmultiple-choice questions No 11")
assert round(approx_sinh(1 , 10), 2) == 1.18
print (round(approx_sinh(3.14, 10), 2))

def approx_cosh(x, n):
    cosh_x = 0
    for i in range(n+1):
        cosh_x += (x ** (2*i)) / factorial(2*i)
    return cosh_x

print(f"\nmultiple-choice questions No 12")
assert round(approx_cosh(1, 10), 2) == 1.54
print(round(approx_cosh(3.14, 10), 2))


print(approx_sin( x =3.14 , n =10))
print(approx_cos( x =3.14 , n =10))
print(approx_sinh( x =3.14 , n =10))
print(approx_cosh( x =3.14 , n =10))

