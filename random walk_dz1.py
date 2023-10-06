import random
import math

def random_walk(n):
    position = 0
    above_ox_count = 0
    above_ox_count_copy = 0
    under_ox_count = 0
    under_ox_count_copy = 0
    sign_changes = 0

    for _ in range(n):
        step = random.choice([1, -1])
        position += step
        if position > 0:
            above_ox_count += 1
            above_ox_count_copy = above_ox_count
        if position < 0:
            under_ox_count += 1
            under_ox_count_copy = under_ox_count

        if (above_ox_count_copy > 0 and under_ox_count_copy > 0):
            sign_changes += 1
            above_ox_count_copy = 0
            under_ox_count_copy = 0

    return above_ox_count, sign_changes

# a) Емпірична ймовірність, що процес був вище ОХ
n = 100
above_ox_count, _ = random_walk(n)
empirical_prob_a = above_ox_count/n

# a) Теоретична ймовірність, що процес був вище ОХ
theoretical_prob_a = math.comb(2*n, n)/2**(2*n)

# b) Емпірична ймовірність кількості змін знаку
_, sign_changes = random_walk(n)
empirical_prob_b = sign_changes / n

# c) Оцінка теоретичної ймовірності останнього попадання в 0 до 10, 15, 20, 50 кроку
def theoretical_prob_last_to_zero(k):
    prob_zero_before_k = 0
    for j in range(1, int(k/2)):
        if j % 2 == 0:
            prob_zero_before_k += (math.comb(2*n, n)/2**(2*n))*(math.comb(2*n-2*j, n-j)/2**(2*n-2*j))
        else:
            prob_zero_before_k += (math.comb(2*n, n)/2**(2*n))*(math.comb(2*n-2*(j-1), n-(j-1))/2**(2*n-2*(j-1)))

    return prob_zero_before_k

k_values = [10, 15, 20, 50]
theoretical_probs_c = [theoretical_prob_last_to_zero(k) for k in k_values]

# c) Розрахунок емпіричної ймовірності для 1000 траєкторій останнього попадання в 0 до 100, 150, 200, 500 кроку

def random_walk_to_zero(l):
    position = 0
    zero_count = 0
    full_zero_count = 0
    for c in range(1000):
        step = random.choice([-1, 1])
        position += step
        if position == 0 and c<=l:
            zero_count += 1
        if position == 0:
            full_zero_count += 1

    return zero_count/full_zero_count

l_values = [100, 150, 200, 500]
empirical_probs_c = [random_walk_to_zero(l) for l in l_values]


# Виведення результатів
print("a) Емпірична ймовірність, що процес був вище ОХ: {}".format(empirical_prob_a))
print("a) Теоретична ймовірність, що процес був вище ОХ: {}".format(theoretical_prob_a))
print("b) Емпірична ймовірність кількості змін знаку: {}".format(empirical_prob_b))
print("c) Теоретичні ймовірності:")
for i, k in enumerate(k_values):
    print("    Для k = {}: {}".format(k, theoretical_probs_c[i]))
print("c) Емпіричні ймовірності для 1000 кроків:")
for c, l in enumerate(l_values):
    print("    Для l = {}: {}".format(l, empirical_probs_c[c]))
