
print("Введите путь до файла: ")
way = input()
with open(f"{way}", "r") as file:
    try:
        array1 = [arr for arr in file.readlines()]
        array = [int(float(arr)) for arr in array1 if arr != "\n"]
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
