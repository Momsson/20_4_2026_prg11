from sorting import random_numbers

class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores
        self._sorted_scores = None  # cache pro bonus

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        points = self.scores[index]

        if points >= 90:
            return "A"
        elif points >= 80:
            return "B"
        elif points >= 70:
            return "C"
        elif points >= 60:
            return "D"
        elif points >= 50:
            return "E"
        else:
            return "F"

    def find(self, score):
        result = []
        for i in range(len(self.scores)):
            if self.scores[i] == score:
                result.append(i)
        return result

    def get_sorted(self):
        scores = self.scores.copy()
        n = len(scores)
        for i in range(n):
            for j in range(0, n - i - 1):
                if scores[j] > scores[j + 1]:
                    scores[j], scores[j + 1] = scores[j + 1], scores[j]

        return scores

    # BONUS: binární vyhledávání s cache
    def find_sorted(self, score):
        if self._sorted_scores is None:
            print("sorting…")
            self._sorted_scores = self.get_sorted()

        arr = self._sorted_scores
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == score:
                return mid
            elif arr[mid] < score:
                left = mid + 1
            else:
                right = mid - 1

        return None


def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    # počet studentů
    print("Počet studentů:", results.count())

    # výpis všech studentů
    for i in range(results.count()):
        points = results.get_by_index(i)
        grade = results.get_grade(i)
        print(f"Student {i}: {points} points – {grade}")

    # hledání
    print("Indexy studentů se 100 body:", results.find(100))
    print("Indexy studentů se 50 body:", results.find(50))
    print("Indexy studentů se 77 body:", results.find(77))
    # seřazený seznam
    print("Seřazené výsledky:", results.get_sorted())
    print("Původní seznam:", results.scores)

    # BONUS: cache
    print(results.find_sorted(91))
    print(results.find_sorted(50))
    print(results.find_sorted(77))

    # náhodná data
    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print("\nNáhodná data:")
    print("Počet:", random_results.count())
    print("Seřazené:", random_results.get_sorted())


if __name__ == "__main__":
    main()
