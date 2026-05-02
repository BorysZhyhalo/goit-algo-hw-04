import random
import sys
import timeit
from collections.abc import Callable


SortFunction = Callable[[list[int]], list[int]]


def configure_output() -> None:
    sys.stdout.reconfigure(encoding="utf-8")


def insertion_sort(data: list[int]) -> list[int]:
    """Сортування вставками: просте, але повільне на великих масивах."""
    numbers = data.copy()

    for i in range(1, len(numbers)):
        current = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > current:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = current

    return numbers


def merge_sort(data: list[int]) -> list[int]:
    """Сортування злиттям: ділить масив навпіл і зливає відсортовані частини."""
    if len(data) <= 1:
        return data.copy()

    middle = len(data) // 2
    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])

    return merge(left, right)


def merge(left: list[int], right: list[int]) -> list[int]:
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


def timsort(data: list[int]) -> list[int]:
    """Вбудований Timsort у Python, доступний через sorted()."""
    return sorted(data)


def generate_data(size: int) -> dict[str, list[int]]:
    random_data = [random.randint(0, size) for _ in range(size)]
    sorted_data = list(range(size))
    reversed_data = list(range(size, 0, -1))
    nearly_sorted_data = sorted_data.copy()

    # Невелика кількість перестановок імітує майже відсортований набір даних.
    for _ in range(size // 20):
        first = random.randint(0, size - 1)
        second = random.randint(0, size - 1)
        nearly_sorted_data[first], nearly_sorted_data[second] = (
            nearly_sorted_data[second],
            nearly_sorted_data[first],
        )

    return {
        "random": random_data,
        "sorted": sorted_data,
        "reversed": reversed_data,
        "nearly sorted": nearly_sorted_data,
    }


def measure_time(sort_function: SortFunction, data: list[int], repeats: int = 3) -> float:
    timer = timeit.Timer(lambda: sort_function(data))
    results = timer.repeat(repeat=repeats, number=1)

    return min(results)


def print_result(
    size: int,
    data_type: str,
    algorithm_name: str,
    execution_time: float,
) -> None:
    print(f"{size:<8} {data_type:<15} {algorithm_name:<15} {execution_time:.6f} сек.")


def run_tests() -> None:
    algorithms: dict[str, SortFunction] = {
        "Insertion sort": insertion_sort,
        "Merge sort": merge_sort,
        "Timsort": timsort,
    }

    sizes = [100, 1000, 5000]

    print(f"{'Size':<8} {'Data type':<15} {'Algorithm':<15} Time")
    print("-" * 55)

    for size in sizes:
        datasets = generate_data(size)

        for data_type, data in datasets.items():
            for algorithm_name, sort_function in algorithms.items():
                execution_time = measure_time(sort_function, data)
                print_result(size, data_type, algorithm_name, execution_time)

        print("-" * 55)


def print_conclusions() -> None:
    print("\nВисновки:")
    print("- Insertion sort має складність O(n^2), тому швидко сповільнюється на великих масивах.")
    print("- Merge sort має складність O(n log n) і працює стабільніше на великих наборах даних.")
    print("- Timsort зазвичай найшвидший, бо поєднує ідеї merge sort та insertion sort.")
    print("- Вбудовані sorted() і list.sort() оптимізовані краще, ніж прості власні реалізації.")


def main() -> None:
    configure_output()
    random.seed(42)
    run_tests()
    print_conclusions()


if __name__ == "__main__":
    main()
