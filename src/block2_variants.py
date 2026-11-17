import random

random.seed(42)


def run_b2_v3(n=100000):
    print("===== БЛОК 2 - Варіант 3 =====")
    p1, p2, p3 = 0.40, 0.40, 0.20
    pc1, pc2, pc3 = 0.05, 0.02, 0.10

    th_c = p1 * pc1 + p2 * pc2 + p3 * pc3
    th_h3c = (p3 * pc3) / th_c

    cc, ch3c = 0, 0
    for _ in range(n):
        r = random.random()
        if r < p1:
            h, pc = 1, pc1
        elif r < p1 + p2:
            h, pc = 2, pc2
        else:
            h, pc = 3, pc3

        if random.random() < pc:
            cc += 1
            if h == 3:
                ch3c += 1

    wc = cc / n
    wh3c = ch3c / cc if cc > 0 else 0

    print(f"Кількість симуляцій: {n}")
    print(
        f"Повна ймовірність P(C)   | Статистична: {wc:.5f} | Теоретична: {th_c:.5f} | Похибка: {abs(wc - th_c):.5f}"
    )
    print(
        f"Апостеріорна P(H3|C)     | Статистична: {wh3c:.5f} | Теоретична: {th_h3c:.5f} | Похибка: {abs(wh3c - th_h3c):.5f}\n"
    )


def run_b4_v3(n=100000):
    print("===== БЛОК 4 - Варіант 3 =====")
    p1, p2 = 0.99, 0.01
    pa1, pa2 = 0.005, 0.95

    pa = p1 * pa1 + p2 * pa2
    th_h2a = (p2 * pa2) / pa
    th_h1a = (p1 * pa1) / pa
    threshold = 0.50

    ca, ch2a = 0, 0
    for _ in range(n):
        is_att = random.random() < p2
        pa_cur = pa2 if is_att else pa1

        if random.random() < pa_cur:
            ca += 1
            if is_att:
                ch2a += 1

    wh2a = ch2a / ca if ca > 0 else 0
    err = abs(wh2a - th_h2a)

    print(f"Змодельовано сесій входів: {n}")
    print(f"Теоретична ймовірність P(H2|A):     {th_h2a:.5f} (P(H1|A) = {th_h1a:.5f})")
    print(
        f"Поріг прийняття рішення (MAP):      {threshold:.2f} (Блокувати, оскільки {th_h2a:.4f} > {threshold:.2f})"
    )
    print(f"Експериментальна частота W(H2|A):   {wh2a:.5f}")
    print(f"Абсолютна похибка результату:       {err:.5f}\n")


if __name__ == "__main__":
    run_b2_v3(n=100000)
    run_b4_v3(n=100000)
