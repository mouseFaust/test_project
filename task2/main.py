try:
    print("Введите массив значений: ")
    array = [int(float(arr)) for arr in input().split()]
    central_value = int(sum(array) / len(array))
    counter = 0
    for arr in array:
        while arr != central_value:
            if arr < central_value:
                arr += 1
            else:
                arr -= 1
            counter += 1
    print(f"{counter}")
except:
    print("Введены неверные данные")
