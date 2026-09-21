

def while1(a, b):
    rest = a
    while rest >= b:
        rest -= b
    return rest


def while2(a, b):
    count = 0
    rest = a
    while rest >= b:
        rest -= b
        count += 1
    return count


def while3(n, k):
    quotient = 0
    rest = n
    while rest >= k:
        rest -= k
        quotient += 1
    return quotient, rest



def while4(n):
    while n % 3 == 0:
        n //= 3
    return n == 1


def while5(n):
    k = 0
    while n > 1:
        n //= 2
        k += 1
    return k


def while6(n):
    product = 1.0
    k = n
    while k > 1:
        product *= k
        k -= 2
    return product


def while7(n):
    k = 1
    while k * k <= n:
        k += 1
    return k


def while8(n):
    k = 1
    while (k + 1) * (k + 1) <= n:
        k += 1
    return k


def while9(n):
    k = 1
    power = 3
    while power <= n:
        power *= 3
        k += 1
    return k


def while10(n):
    k = 0
    power = 1
    while power * 3 < n:
        power *= 3
        k += 1
    return k




def while11(n):
    k = 1
    total = 1
    while total < n:
        k += 1
        total += k
    return k, total


def while12(n):
    k = 1
    total = 1
    while total + k + 1 <= n:
        k += 1
        total += k
    return k, total


def while13(a):
    k = 1
    total = 1.0
    while total <= a:
        k += 1
        total += 1 / k
    return k, total


def while14(a):
    k = 1
    total = 1.0
    while total + 1 / (k + 1) < a:
        k += 1
        total += 1 / k
    return k, total


def while15(p):
    s = 1000.0
    k = 0
    while s <= 1100:
        s *= 1 + p / 100
        k += 1
    return k, s


def while16(p):
    day = 10.0
    total = 0.0
    k = 0
    while total <= 200:
        total += day
        k += 1
        day *= 1 + p / 100
    return k, total




def while17(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    return digits


def while18(n):
    count = 0
    total = 0
    while n > 0:
        total += n % 10
        count += 1
        n //= 10
    return count, total


def while19(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev


def while20(n):
    while n > 0:
        if n % 10 == 2:
            return True
        n //= 10
    return False


def while21(n):
    while n > 0:
        if n % 10 % 2 == 1:
            return True
        n //= 10
    return False


def while22(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:         
        if n % d == 0:
            return False
        d += 1
    return True



def while23(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def while24(n):
    a, b = 1, 1
    while b < n:
        a, b = b, a + b
    return b == n


def while25(n):
    a, b = 1, 1
    while b <= n:
        a, b = b, a + b
    return b


def while26(n):
    a, b = 1, 1
    while b < n:
        a, b = b, a + b
    return a, a + b


def while27(n):
    a, b = 1, 1
    k = 2
    while b < n:
        a, b = b, a + b
        k += 1
    return k



def while28(eps):
    prev = 2.0
    cur = 2 + 1 / prev
    k = 2
    while abs(cur - prev) >= eps:
        prev = cur
        cur = 2 + 1 / cur
        k += 1
    return k, prev, cur


def while29(eps):
    a1, a2 = 1.0, 2.0
    k = 2
    while abs(a2 - a1) >= eps:
        a1, a2 = a2, (a1 + 2 * a2) / 3
        k += 1
    return k, a1, a2


def while30(a, b, c):
    count = 0
    rest_a = a
    while rest_a >= c:          
        rest_a -= c
        rest_b = b
        while rest_b >= c:      
            rest_b -= c
            count += 1
    return count


