import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(cislo):
    cislo = cislo.copy()
    n = len(cislo)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if cislo[j] < cislo[min_idx]:
                min_idx = j
        cislo[i], cislo[min_idx] = cislo[min_idx], cislo[i]

    return cislo

if __name__ == "__main__":
#kratky seznam
        test_list = [5, 1, 4, 2, 8]
        print("Puvodní seznam:", test_list)
        print("Serazený seznam:", selection_sort(test_list))
# 20 cisiel
        random_list = random_numbers(20)
        print("Náhodný seznam:", random_list)
        print("Serazený náhodný seznam:", selection_sort(random_list))