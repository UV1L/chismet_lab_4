import sys
import math

x_0 = 2
x_n = 3


def f(x): return math.cos(x) / (x + 1)


def f2(_x_0, _x_n): return (_x_n - _x_0) / 8 * (f(_x_0) + 3 * f((2 * _x_0 + _x_n) / 3) + 3 * f((_x_0 + 2 * _x_n) / 3) + f(_x_n))


def get_error(s1, s2, s3):
    err1 = 2 * (s2 - s1)
    err2 = s2 - s1
    err3 = s3 - s2

    return err1, err2, err3


def get_error_3_8(s1, s2, s3):
    err1 = (s2 - s1) * 16 / 15
    err2 = (s2 - s1) * 1 / 15
    err3 = (s3 - s2) * 1 / 15

    return err1, err2, err3


def get_actual_error(h, errors):
    actual_error = 0
    if h == 0.1:
        actual_error = errors[0]
    if h == 0.05:
        actual_error = errors[1]
    if h == 0.025:
        actual_error = errors[2]

    return actual_error


def get_points(h):
    x = x_0
    result = []
    while x < x_n:
        result.append(x)
        x += h
    if abs(result[len(result) - 1] - x_n) > 0.01:
        result.append(x_n)

    return result


def f_trapezoid(h):
    n = int((x_n - x_0) / h)
    f_sum = 0
    for i in range(n):
        if i > 0:
            f_sum += f(x_0 + i * h)

    return h * ((f(x_0) + f(x_n)) / 2 + f_sum)


def f_3_8(h):
    points = get_points(h)
    result = 0
    for i in range(len(points) - 1):
        result += f2(points[i], points[i + 1])

    return result


def main():
    h = float(sys.argv[1])
    result_trapezoid = f_trapezoid(h)
    result_3_8 = f_3_8(h)
    errors_trapezoid = get_error(f_trapezoid(0.1), f_trapezoid(0.05), f_trapezoid(0.025))
    errors_3_8 = get_error_3_8(f_3_8(0.1), f_3_8(0.05), f_3_8(0.025))

    print()
    print("----Метод трапеций----")
    print(result_trapezoid)
    print("----Погрешность----")
    print(errors_trapezoid)
    print("----Реальный результат----")
    print(result_trapezoid + get_actual_error(h, errors_trapezoid))
    print()
    print("----Метод 3/8----")
    print(result_3_8)
    print("----Погрешность----")
    print(errors_3_8)
    print("---Реальный результат----")
    print(result_3_8 + get_actual_error(h, errors_3_8))
    print()


if __name__ == '__main__':
    main()
