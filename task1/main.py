try:
    print("Введите длину массива n и длину комбинаций m: ")
    data = [int(float(arr)) for arr in input().split()]
    n = data[0]
    array = list(range(1, n + 1))
    m = data[1]
    result = []
    result.append(array[0])
    i = 0
    while True:
        i = i + m - 1
        i = i % n
        if i == 0:
            break
        result.append(array[i])
    for arr in result:
        print(f"{arr}\n")
except:
    print("Введены неверные данные")
