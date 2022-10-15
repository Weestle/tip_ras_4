import math

# Вариант 5

K = 4.0
L = 2.4
# a = (K - L) / 2
# b = K + L
a = 0
b = 1


def exact_I(x):
    global K, L
    return 0.5 * math.log(x ** 2 + x + K) + (L - 0.5) / (K - 0.25) ** 0.5 * math.atan((x + 0.5) / (K - 0.25) ** 0.5)


def F(x):
    global K, L
    return 1 / (1 + x)
    # return (x + L) / (x ** 2 + x + K)


def trapezoid(n):
    global a, b
    I = 0
    h = (b - a) / n
    for i in range(1, n):
        x = a + i * h
        I += 2 * F(x)
    I = (I + a + b) * h / 2
    print(I)


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
    print(I)


def
# trapezoid(4)
# trapezoid(6)
# trapezoid(8)
# parabola(4)
# parabola(6)
# parabola(8)
