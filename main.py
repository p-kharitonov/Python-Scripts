import random


def get_random_elem(arr: list) -> any:
    return random.choices(arr, weights=[i for i in range(len(arr), 0, -1)])[0]


def tester(arr: list) -> str:
    my_dict = {}
    result = ''
    for elem in arr:
        my_dict[elem] = 0
    for _ in range(1000000):
        a = get_random_elem(arr)
        my_dict[a] += + 1
    for elem in arr:
        result += f'{elem} - {my_dict[elem]}\n'
    return result


def main():
    my_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'apple', 11, 12, 13]
    print(get_random_elem(my_arr))


if __name__ == "__main__":
    main()
