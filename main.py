import math

# Вариант 5

# K = 4.0
# L = 2.4


K = float(input('K = '))
L = float(input('L = '))
a = (K - L) / 2
b = K + L

def exact_I(x):
    global K, L
    return 0.5 * math.log(x ** 2 + x + K) + (L - 0.5) / (K - 0.25) ** 0.5 * math.atan((x + 0.5) / (K - 0.25) ** 0.5)

def range_exact_I():
    global a, b
    return exact_I(b) - exact_I(a)

def F(x):
    global K, L
    return (x + L) / (x ** 2 + x + K)


def trapezoid(n):
    global a, b
    I = 0
    h = (b - a) / n
    for i in range(1, n):
        x = a + i * h
        I += 2 * F(x)
    I = (I + F(a) + F(b)) * h / 2
    return I


def parabola(n):
    global a, b
    I = 0
    h = (b - a) / 2 / n
    c = 1
    for i in range(1, n * 2):
        x = a + i * h
        if c % 2 == 1:
            I += 4 * F(x)
        else:
            I += 2 * F(x)
        c += 1
    I = (I + F(a) + F(b)) * h / 3
    return I




def gauss(n):
    ti4 = [0.861136, 0.339981]
    ti6 = [0.932464, 0.661209, 0.238619]
    ti8 = [0.960289, 0.796666, 0.525532, 0.183434]
    A4 = [0.347854, 0.652145]
    A6 = [0.171324, 0.360761, 0.467913]
    A8 = [0.101228, 0.222381, 0.313706, 0.362683]

    if n == 4:
        ti = ti4
        A = A4
    if n == 6:
        ti = ti6
        A = A6
    if n == 8:
        ti = ti8
        A = A8
    # print(A)
    I = 0
    for i in range(int(n / 2)):
        I += A[i] * F((a + b) / 2 + (b - a) / 2 * ti[i])
        I += A[i] * F((a + b) / 2 - (b - a) / 2 * ti[i])
        # print(A[i], F((a + b) / 2 + (b - a) / 2 * ti[i]))
        # print(A[i], F((a + b) / 2 - (b - a) / 2 * ti[i]))
    I *= (b - a) / 2
    return I


trapezoid(4)

print('%-10s %-20s %-20s %-20s' % ('n', '4', '6', '8'))
print('%-10s %-20s %-20s %-20s' % ('Iтр', trapezoid(4), trapezoid(6), trapezoid(8)))
print('%-10s %-20s %-20s %-20s' % ('Iпар', parabola(4), parabola(6), parabola(8)))
print('%-10s %-20s %-20s %-20s' % ('Ig', gauss(4), gauss(6), gauss(8)))
print('%-10s %-20s %-20s %-20s' % ('Ireal', range_exact_I(), range_exact_I(), range_exact_I()))
