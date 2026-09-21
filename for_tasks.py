

def hdr(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def f(x, nd=4):
    return f"{x:.{nd}f}"


def for1(K, N):
    for _ in range(N):
        print(K, end=" ")
    print()


def for2(A, B):
    nums = list(range(A, B + 1))
    print(" ".join(map(str, nums)))
    print("N =", len(nums))


def for3(A, B):
    nums = list(range(B - 1, A, -1))
    print(" ".join(map(str, nums)))
    print("N =", len(nums))



def for4(price):
    for kg in range(1, 11):
        print(f"{kg} кг -> {f(price * kg, 2)}")


def for5(price):
    for i in range(1, 11):
        weight = i / 10
        print(f"{f(weight, 1)} кг -> {f(price * weight, 2)}")


def for6(price):
    for i in range(1, 6):
        weight = 1.0 + i * 0.2          
        print(f"{f(weight, 1)} кг -> {f(price * weight, 2)}")



def for7(A, B):
    s = 0
    for i in range(A, B + 1):
        s += i
    print("Сумма =", s)


def for8(A, B):
    p = 1
    for i in range(A, B + 1):
        p *= i
    print("Произведение =", p)


def for9(A, B):
    s = 0
    for i in range(A, B + 1):
        s += i * i
    print("Сумма квадратов =", s)


def for10(N):
    s = 0.0
    for i in range(1, N + 1):
        s += 1.0 / i
    print("Сумма =", f(s, 6))


def for11(N):
    s = 0
    for i in range(N, 2 * N + 1):
        s += i * i
    print("Сумма =", s)



def for12(N):
    p = 1.0
    for i in range(1, N + 1):
        p *= 1.0 + 0.1 * i              
    print("Произведение =", f(p, 6))


def for13(N):
    s = 0.0
    sign = 1.0
    for i in range(N):
        s += sign * (1.0 + 0.1 * (i + 1))
        sign = -sign                   
    print("Значение =", f(s, 6))


def for14(N):
    s = 0
    for i in range(1, N + 1):
        s += 2 * i - 1
        print(f"После {i}-го слагаемого сумма = {s}   (= {i}^2)")
    print(f"N^2 = {s}")


def for15(A, N):
    p = 1.0
    for _ in range(N):
        p *= A
    print(f"A^N = {f(p, 6)}")


def for16(A, N):
    p = 1.0
    for i in range(1, N + 1):
        p *= A
        print(f"A^{i} = {f(p, 6)}")


def for17(A, N):
    s = 0.0
    p = 1.0                            
    for _ in range(N + 1):
        s += p
        p *= A
    print("Сумма =", f(s, 6))


def for18(A, N):
    s = 0.0
    p = 1.0
    sign = 1.0
    for _ in range(N + 1):
        s += sign * p
        p *= A
        sign = -sign
    print("Значение =", f(s, 6))


def for19(N):
    p = 1.0
    for i in range(1, N + 1):
        p *= i
    print(f"{N}! = {f(p, 6)}")


def for20(N):
    s = 0.0
    fact = 1.0
    for i in range(1, N + 1):
        fact *= i                       
        s += fact
    print("Сумма =", f(s, 6))



def for21(N):
    s = 1.0                            
    fact = 1.0
    for i in range(1, N + 1):
        fact *= i
        s += 1.0 / fact
    print(f"Значение = {f(s, 6)}   (e = {f(exp(1), 6)})")


def for22(X, N):
    s = 0.0
    term = 1.0                         
    for i in range(N + 1):
        s += term
        term *= X / (i + 1)             
    print(f"Значение = {f(s, 6)}   (exp(X) = {f(exp(X), 6)})")


def for23(X, N):
    s = 0.0
    fact = 1.0                          
    xpow = X                            
    sign = 1.0
    for k in range(N + 1):
        s += sign * xpow / fact
        fact *= (2 * k + 2) * (2 * k + 3)
        xpow *= X * X
        sign = -sign
    print(f"Значение = {f(s, 6)}   (sin(X) = {f(sin(X), 6)})")


def for24(X, N):
    s = 0.0
    fact = 1.0                         
    xpow = 1.0                         
    sign = 1.0
    for k in range(N + 1):
        s += sign * xpow / fact
        fact *= (2 * k + 1) * (2 * k + 2)
        xpow *= X * X
        sign = -sign
    print(f"Значение = {f(s, 6)}   (cos(X) = {f(cos(X), 6)})")


def for25(X, N):
    s = 0.0
    p = 1.0
    sign = 1.0
    for k in range(1, N + 1):
        p *= X
        s += sign * p / k
        sign = -sign
    print("Значение =", f(s, 6))


def for26(X, N):
    s = 0.0
    xpow = X
    sign = 1.0
    for k in range(N + 1):
        s += sign * xpow / (2 * k + 1)
        xpow *= X * X
        sign = -sign
    print("Значение =", f(s, 6))


def for27(X, N):
    s = X
    term = X                            
    for k in range(1, N + 1):
        term *= X * X * (2 * k - 1) / (2 * k * (2 * k + 1))
        s += term
    print(f"Значение = {f(s, 6)}   (asin(X) = {f(asin(X), 6)})")


def for28(X, N):
    s = 1.0
    coef = 1.0                          
    p = 1.0
    for k in range(1, N + 1):
        coef *= -1.0 * (2 * k - 3) / (2 * k)
        p *= X
        s += coef * p
    print(f"Значение = {f(s, 6)}   (sqrt(1+X) = {f(sqrt(1 + X), 6)})")



def for29(N, A, B):
    H = (B - A) / N
    print(f"H = {f(H, 6)}")
    points = [A + i * H for i in range(N + 1)]
    print(" ".join(f(p, 6) for p in points))


def for30(N, A, B):
    H = (B - A) / N
    print(f"H = {f(H, 6)}")
    for i in range(N + 1):
        x = A + i * H
        print(f"F({f(x, 4)}) = {f(1 - sin(x), 6)}")



def for31(N):
    a = 2.0                             
    for k in range(1, N + 1):
        a = 2 + 1 / a
        print(f"A{k} = {f(a, 6)}")


def for32(N):
    a = 1.0                            
    for k in range(1, N + 1):
        a = (a + 1) / k
        print(f"A{k} = {f(a, 6)}")


def for33(N):
    f_prev, f_cur = 1, 1
    seq = [f_prev, f_cur]
    for _ in range(3, N + 1):
        f_prev, f_cur = f_cur, f_prev + f_cur
        seq.append(f_cur)
    print(" ".join(map(str, seq[:N])))


def for34(N):
    a1, a2 = 1.0, 2.0
    print(f"A1 = {f(a1, 6)}")
    if N >= 2:
        print(f"A2 = {f(a2, 6)}")
    for k in range(3, N + 1):
        a1, a2 = a2, (a1 + 2 * a2) / 3
        print(f"A{k} = {f(a2, 6)}")


def for35(N):
    seq = [1, 2, 3]
    for k in range(4, N + 1):
        seq.append(seq[-1] + seq[-2] - 2 * seq[-3])
    print(" ".join(map(str, seq[:N])))



def for36(N, K):
    s = 0.0
    for i in range(1, N + 1):
        s += float(i) ** K
    print("Сумма =", f(s, 6))


def for37(N):
    s = 0.0
    for i in range(1, N + 1):
        s += float(i) ** i
    print("Сумма =", f(s, 6))


def for38(N):
    s = 0.0
    for i in range(1, N + 1):
        s += float(i) ** (N + 1 - i)
    print("Сумма =", f(s, 6))


def for39(A, B):
    for x in range(A, B + 1):
        print(" ".join([str(x)] * x))


def for40(A, B):
    for x in range(A, B + 1):
        print(" ".join([str(x)] * (x - A + 1)))

