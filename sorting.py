import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

#selection short

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
# bubble short
def bubble_sort(cislo):
    sort = cislo.copy()
    n = len(sort)


    plt.ion()
    plt.show()

    for i in range(n):
        for j in range(0, n - i - 1):

            # vizualizace
            index_highlight1 = j
            index_highlight2 = j + 1
            colors = ["steelblue"] * len(sort)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"

            plt.clf()
            plt.bar(range(len(sort)), sort, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)

            if sort[j] > sort[j + 1]:
                sort[j], sort[j + 1] = sort[j + 1], sort[j]

    plt.ioff()
    plt.show()

    return sort

if __name__ == "__main__":
    # krátký seznam
    test_list = [5, 1, 4, 2, 8]
    print("Původní seznam:", test_list)
    print("Seřazený seznam SS:", selection_sort(test_list))
    print("Seřazený seznam BS:", bubble_sort(test_list))

    # 20 čísel
    random_list = random_numbers(200)
    print("Náhodný seznam:", random_list)
    print("Seřazený náhodný seznam SS:", selection_sort(random_list))
    print("Seřazený seznam BS:", bubble_sort(random_list))