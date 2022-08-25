# 문제
# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.
#
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.
#
# 출력
# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
#
# 둘째 줄에는 중앙값을 출력한다.
#
# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
#
# 넷째 줄에는 범위를 출력한다.

def merge_array(array1, array2):
    array1_idx = 0
    array2_idx = 0

    new_array = []

    while True:
        if array1[array1_idx] < array2[array2_idx]:
            new_array.append(array1[array1_idx])
            array1_idx += 1
        else:
            new_array.append(array2[array2_idx])
            array2_idx += 1

        if array1_idx == len(array1):
            new_array.extend(array2[array2_idx:])
            return new_array

        if array2_idx == len(array2):
            new_array.extend(array1[array1_idx:])
            return new_array


def merge_sort(array):
    n = len(array)

    if n <= 1:
        return array

    middle_idx = int(n / 2)

    array1 = merge_sort(array[:middle_idx])
    array2 = merge_sort(array[middle_idx:])

    return merge_array(array1, array2)



def average(num_list):
    total_num = 0

    for num in num_list:
        total_num += num

    return int(round(total_num / len(num_list), 0))


def middle_num(num_list):
    middle_idx = int(len(num_list) / 2)

    sorted_list = merge_sort(num_list)

    return sorted_list[middle_idx]


def max_frequency_num(num_list):
    freq_dict = dict()

    for num in num_list:
        freq_of_num = freq_dict.get(num, None)

        if freq_of_num is None:
            freq_dict[num] = 1
        else:
            freq_dict[num] += 1

    max_freq = 0
    max_freq_num_list = []

    for num, freq in freq_dict.items():
        if freq > max_freq:
            max_freq_num_list = [num]
            max_freq = freq
        elif freq == max_freq:
            max_freq_num_list.append(num)

    if len(max_freq_num_list) == 1:
        return max_freq_num_list[0]

    sorted_list = merge_sort(max_freq_num_list)

    return sorted_list[1]


def range_of_list(num_list):
    if len(num_list) <= 1:
        return 0

    sorted_list = merge_sort(num_list)
    return sorted_list[-1] - sorted_list[0]


def main():
    n = int(input("input N : "))

    num_list = [int(input("input Number : ")) for _ in range(n)]

    print(average(num_list))
    print(middle_num(num_list))
    print(max_frequency_num(num_list))
    print(range_of_list(num_list))


main()