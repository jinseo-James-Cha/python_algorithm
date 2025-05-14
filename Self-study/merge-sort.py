# MergeSort(0, N) = Merge(MergeSort(0, N/2) + MergeSort(N/2, N))

def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_array = array[:mid]
    right_array = array[mid:]
    print(left_array)
    print(right_array)
    return merge(merge_sort(left_array), merge_sort(right_array))

def merge(array1, array2):
    array_c = []

    index_1 = 0
    index_2 = 0
    while len(array1) > index_1 and len(array2) > index_2:
        if array1[index_1] > array2[index_2]:
            array_c.append(array2[index_2])
            index_2 += 1
        else:
            array_c.append(array1[index_1])
            index_1 += 1

    return array_c + array1[index_1:] + array2[index_2:]

array = [5, 3, 2, 1, 6, 8, 7, 4]


print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge_sort([-7, -1, 9, 40, 5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge_sort([-1, 2, 3, 5, 40, 10, 78, 100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge_sort([-1, -1, 0, 1, 6, 9, 10]))