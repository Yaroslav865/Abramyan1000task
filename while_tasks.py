"""
Задачник М. Э. Абрамяна (Programming Taskbook 4.4) — группа While
("Цикл с условием"). Задачи While1–While30.

Формат:
  * каждая задача — отдельная функция while1 ... while30 с номером в имени
    и короткой строкой-описанием в docstring;
  * входные данные заданы прямо в коде, в блоке if __name__ == "__main__" —
    меняйте значения там (по одному примеру на задачу);
  * при запуске на экран выводится имя задачи и её результат.

Запуск:  python while_tasks.py
"""


# ----------------------------------------------------------------------
#  While1 – While3  (арифметика без умножения и деления)
# ----------------------------------------------------------------------

def while1(a, b):
    """While1*. Незанятая часть отрезка длины A после размещения отрезков B
    (то есть остаток A mod B), без умножения и деления."""
    rest = a
    while rest >= b:
        rest -= b
    return rest


def while2(a, b):
    """While2*. Количество отрезков длины B, размещённых на отрезке A,
    без умножения и деления."""
    count = 0
    rest = a
    while rest >= b:
        rest -= b
        count += 1
    return count


def while3(n, k):
    """While3. Частное и остаток от деления N на K нацело,
    только сложение и вычитание."""
    quotient = 0
    rest = n
    while rest >= k:
        rest -= k
        quotient += 1
    return quotient, rest


# ----------------------------------------------------------------------
#  While4 – While10  (степени и квадраты)
# ----------------------------------------------------------------------

def while4(n):
    """While4*. Является ли N степенью числа 3."""
    while n % 3 == 0:
        n //= 3
    return n == 1


def while5(n):
    """While5. N = 2^K — найти показатель K."""
    k = 0
    while n > 1:
        n //= 2
        k += 1
    return k


def while6(n):
    """While6. Двойной факториал N!! = N*(N-2)*(N-4)*...
    (вещественный результат против переполнения)."""
    product = 1.0
    k = n
    while k > 1:
        product *= k
        k -= 2
    return product


def while7(n):
    """While7*. Наименьшее целое K, для которого K^2 > N
    (функцию извлечения корня не используем)."""
    k = 1
    while k * k <= n:
        k += 1
    return k


def while8(n):
    """While8. Наибольшее целое K, для которого K^2 <= N
    (функцию извлечения корня не используем)."""
    k = 1
    while (k + 1) * (k + 1) <= n:
        k += 1
    return k


def while9(n):
    """While9. Наименьшее целое K, при котором 3^K > N."""
    k = 1
    power = 3
    while power <= n:
        power *= 3
        k += 1
    return k


def while10(n):
    """While10. Наибольшее целое K, при котором 3^K < N."""
    k = 0
    power = 1
    while power * 3 < n:
        power *= 3
        k += 1
    return k


# ----------------------------------------------------------------------
#  While11 – While16  (суммы, вклад, лыжник)
# ----------------------------------------------------------------------

def while11(n):
    """While11*. Наименьшее K с суммой 1+2+...+K >= N и сама сумма."""
    k = 1
    total = 1
    while total < n:
        k += 1
        total += k
    return k, total


def while12(n):
    """While12*. Наибольшее K с суммой 1+2+...+K <= N и сама сумма."""
    k = 1
    total = 1
    while total + k + 1 <= n:
        k += 1
        total += k
    return k, total


def while13(a):
    """While13. Наименьшее K, для которого 1 + 1/2 + ... + 1/K > A,
    и сама сумма."""
    k = 1
    total = 1.0
    while total <= a:
        k += 1
        total += 1 / k
    return k, total


def while14(a):
    """While14. Наибольшее K, для которого 1 + 1/2 + ... + 1/K < A,
    и сама сумма."""
    k = 1
    total = 1.0
    while total + 1 / (k + 1) < a:
        k += 1
        total += 1 / k
    return k, total


def while15(p):
    """While15. Вклад 1000 руб., +P% в месяц: через сколько месяцев K
    сумма превысит 1100 руб. и итоговый размер S."""
    s = 1000.0
    k = 0
    while s <= 1100:
        s *= 1 + p / 100
        k += 1
    return k, s


def while16(p):
    """While16. Лыжник: 10 км в 1-й день, +P% к пробегу каждый день.
    День K, после которого суммарный пробег > 200 км, и сам пробег S."""
    day = 10.0
    total = 0.0
    k = 0
    while total <= 200:
        total += day
        k += 1
        day *= 1 + p / 100
    return k, total


# ----------------------------------------------------------------------
#  While17 – While22  (цифры числа)
# ----------------------------------------------------------------------

def while17(n):
    """While17. Все цифры числа N, начиная с младшего разряда."""
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    return digits


def while18(n):
    """While18. Количество и сумма цифр числа N."""
    count = 0
    total = 0
    while n > 0:
        total += n % 10
        count += 1
        n //= 10
    return count, total


def while19(n):
    """While19. Число, полученное при чтении N справа налево."""
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev


def while20(n):
    """While20. Есть ли в записи числа N цифра «2»."""
    while n > 0:
        if n % 10 == 2:
            return True
        n //= 10
    return False


def while21(n):
    """While21. Есть ли в записи числа N нечётные цифры."""
    while n > 0:
        if n % 10 % 2 == 1:
            return True
        n //= 10
    return False


def while22(n):
    """While22*. Является ли N простым числом."""
    if n < 2:
        return False
    d = 2
    while d * d <= n:          # достаточно проверять делители до sqrt(N)
        if n % d == 0:
            return False
        d += 1
    return True


# ----------------------------------------------------------------------
#  While23 – While27  (НОД и числа Фибоначчи)
# ----------------------------------------------------------------------

def while23(a, b):
    """While23*. НОД(A, B) по алгоритму Евклида."""
    while b != 0:
        a, b = b, a % b
    return a


def while24(n):
    """While24. Является ли N числом Фибоначчи."""
    a, b = 1, 1
    while b < n:
        a, b = b, a + b
    return b == n


def while25(n):
    """While25. Первое число Фибоначчи, большее N."""
    a, b = 1, 1
    while b <= n:
        a, b = b, a + b
    return b


def while26(n):
    """While26. Для N = F_K: предыдущее F_(K-1) и следующее F_(K+1)."""
    a, b = 1, 1
    while b < n:
        a, b = b, a + b
    return a, a + b


def while27(n):
    """While27. Для N = F_K: порядковый номер этого числа Фибоначчи K."""
    a, b = 1, 1
    k = 2
    while b < n:
        a, b = b, a + b
        k += 1
    return k


# ----------------------------------------------------------------------
#  While28 – While30  (сходящиеся последовательности и плитка)
# ----------------------------------------------------------------------

def while28(eps):
    """While28. A1 = 2, A_k = 2 + 1/A_(k-1).
    Первый номер K с |A_k - A_(k-1)| < eps, а также A_(k-1) и A_k."""
    prev = 2.0
    cur = 2 + 1 / prev
    k = 2
    while abs(cur - prev) >= eps:
        prev = cur
        cur = 2 + 1 / cur
        k += 1
    return k, prev, cur


def while29(eps):
    """While29. A1 = 1, A2 = 2, A_k = (A_(k-2) + 2*A_(k-1)) / 3.
    Первый номер K с |A_k - A_(k-1)| < eps, а также A_(k-1) и A_k."""
    a1, a2 = 1.0, 2.0
    k = 2
    while abs(a2 - a1) >= eps:
        a1, a2 = a2, (a1 + 2 * a2) / 3
        k += 1
    return k, a1, a2


def while30(a, b, c):
    """While30. Количество квадратов со стороной C, уложенных без наложений
    на прямоугольник A x B. Операции умножения и деления не используем."""
    count = 0
    rest_a = a
    while rest_a >= c:          # «столбцы» по стороне A
        rest_a -= c
        rest_b = b
        while rest_b >= c:      # «строки» по стороне B
            rest_b -= c
            count += 1
    return count


# ----------------------------------------------------------------------
#  Примеры запуска (данные заданы прямо здесь)
# ----------------------------------------------------------------------

if __name__ == "__main__":
    print("While1  (A=17, B=5)                :", while1(17, 5))
    print("While2  (A=17, B=5)                :", while2(17, 5))
    print("While3  (N=17, K=5)                :", while3(17, 5))

    print("While4  (N=27)                     :", while4(27))
    print("While4  (N=20)                     :", while4(20))
    print("While5  (N=128)                    :", while5(128))
    print("While6  (N=9)                      :", while6(9))
    print("While7  (N=20)                     :", while7(20))
    print("While8  (N=20)                     :", while8(20))
    print("While9  (N=20)                     :", while9(20))
    print("While10 (N=20)                     :", while10(20))

    print("While11 (N=20)                     :", while11(20))
    print("While12 (N=20)                     :", while12(20))
    print("While13 (A=2.0)                    :", while13(2.0))
    print("While14 (A=2.0)                    :", while14(2.0))
    print("While15 (P=5)                      :", while15(5))
    print("While16 (P=10)                     :", while16(10))

    print("While17 (N=12345)                  :", while17(12345))
    print("While18 (N=12345)                  :", while18(12345))
    print("While19 (N=12345)                  :", while19(12345))
    print("While20 (N=12345)                  :", while20(12345))
    print("While20 (N=12325)                  :", while20(12325))
    print("While21 (N=12346)                  :", while21(12346))
    print("While22 (N=17)                     :", while22(17))
    print("While22 (N=21)                     :", while22(21))

    print("While23 (A=1071, B=462)            :", while23(1071, 462))
    print("While24 (N=13)                     :", while24(13))
    print("While24 (N=14)                     :", while24(14))
    print("While25 (N=20)                     :", while25(20))
    print("While26 (N=13)                     :", while26(13))
    print("While27 (N=13)                     :", while27(13))

    print("While28 (eps=0.001)                :", while28(0.001))
    print("While29 (eps=0.001)                :", while29(0.001))
    print("While30 (A=10, B=7, C=3)           :", while30(10, 7, 3))
