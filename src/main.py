import os
import random
import matplotlib.pyplot as plt

random.seed(42)
os.makedirs("graphics", exist_ok=True)


def run_b1():
    print("===== БЛОК 1 =====")
    p1, p2, p3 = 0.90, 0.08, 0.02
    pa1, pa2, pa3 = 0.01, 0.25, 0.90
    p_th = (p3 * pa3) / (p1 * pa1 + p2 * pa2 + p3 * pa3)
    n_vals = [100, 1000, 10000, 100000, 1000000]
    w_list = []

    for n in n_vals:
        ca, ch3a = 0, 0
        for _ in range(n):
            r = random.random()
            if r < p1:
                h, pa = 1, pa1
            elif r < p1 + p2:
                h, pa = 2, pa2
            else:
                h, pa = 3, pa3

            if random.random() < pa:
                ca += 1
                if h == 3:
                    ch3a += 1

        wa = ca / n
        wh3a = ch3a / ca if ca > 0 else 0
        err = abs(wh3a - p_th)
        w_list.append(wh3a)
        print(
            f"N = {n:7d} | W(A)={wa:.4f} | W(H3|A)={wh3a:.4f} | Теорія={p_th:.4f} | Похибка={err:.4f}"
        )

    plt.figure(figsize=(10, 5))
    plt.axhline(
        y=p_th,
        color="g",
        linestyle="--",
        label=f"Теоретичне значення P(H3|A) = {p_th:.4f}",
    )
    plt.plot(
        n_vals, w_list, marker="o", color="b", label="Експериментальна оцінка W(H3|A)"
    )
    plt.xscale("log")
    plt.xlabel("Кількість запитів N (лог. шкала)")
    plt.ylabel("Апостеріорна ймовірність")
    plt.title("Блок 1: Збіжність W(H3|A) до теоретичного байєсівського значення")
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.savefig("graphics/block1_convergence.png")
    plt.close()


def run_b3(n=10000):
    print("\n===== БЛОК 3 =====")
    ps, ph = 0.30, 0.70
    pw1s, pw2s = 0.80, 0.60
    pw1h, pw2h = 0.05, 0.10

    tp, fp, tn, fn = 0, 0, 0, 0

    for _ in range(n):
        is_spam = random.random() < ps
        if is_spam:
            x1 = 1 if random.random() < pw1s else 0
            x2 = 1 if random.random() < pw2s else 0
        else:
            x1 = 1 if random.random() < pw1h else 0
            x2 = 1 if random.random() < pw2h else 0

        score_s = ps * (pw1s if x1 else 1 - pw1s) * (pw2s if x2 else 1 - pw2s)
        score_h = ph * (pw1h if x1 else 1 - pw1h) * (pw2h if x2 else 1 - pw2h)
        pred_spam = score_s > score_h

        if is_spam and pred_spam:
            tp += 1
        elif not is_spam and pred_spam:
            fp += 1
        elif not is_spam and not pred_spam:
            tn += 1
        else:
            fn += 1

    acc = (tp + tn) / n
    prec = tp / (tp + fp) if (tp + fp) > 0 else 0
    rec = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0

    print(f"Матриця помилок: TP={tp}, FP={fp}, TN={tn}, FN={fn}")
    print(f"Accuracy  = {acc:.4f}")
    print(f"Precision = {prec:.4f}")
    print(f"Recall    = {rec:.4f}")
    print(f"F1-score  = {f1:.4f}")

    cm = [[tp, fn], [fp, tn]]
    plt.figure(figsize=(6, 5))
    plt.imshow(cm, cmap="Blues")
    plt.title("Блок 3: Матриця помилок Naive Bayes (N=10000)")
    plt.xticks([0, 1], ["Прогноз: Spam", "Прогноз: Ham"])
    plt.yticks([0, 1], ["Факт: Spam", "Факт: Ham"])
    for i in range(2):
        for j in range(2):
            plt.text(
                j, i, str(cm[i][j]), ha="center", va="center", color="black", fontsize=14
            )
    plt.colorbar()
    plt.tight_layout()
    plt.savefig("graphics/simulation_results.png")
    plt.close()
    print("\n[УСПІХ]: Блоки 1 та 3 виконано, графіки збережено в 'graphics/'!")


if __name__ == "__main__":
    run_b1()
    run_b3()
