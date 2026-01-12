
def convert_tempreture(base_temp, target_temp, num):
    # base_temp = base_temp_menu.get()
    # target_temp = target_temp_menu.get()
    # num = num_entry.get()

    # выбор температур происходит через выпадающие списки
    # ввод числа через текстовое пол



    num = float(num)

    if base_temp == "Fahrenheit" and target_temp == "Fahrenheit":
        converted_num = num
        return f"{converted_num:.2f}"

    elif (base_temp == "Fahrenheit") and (target_temp == "Celsius"):
        converted_num = (num - 32) * (5 / 9)
        return f"{converted_num:.2f}"

    elif (base_temp == "Fahrenheit") and (target_temp == "Kelvin"):
        converted_num = (num + 459.67) * (5 / 9)
        return f"{converted_num:.2f}"

    elif (base_temp == "Celsius") and (target_temp == "Fahrenheit"):
        converted_num = (num * 1.8) + 32
        return f"{converted_num:.2f}"

    elif (base_temp == "Celsius") and (target_temp == "Celsius"):
        converted_num = num
        return f"{converted_num:.2f}"

    elif (base_temp == "Celsius") and (target_temp == "Kelvin"):
        converted_num = num + 273
        return f"{converted_num:.2f}"

    elif (base_temp == "Kelvin") and (target_temp == "Fahrenheit"):
        converted_num = 1.8 * (num - 273) + 32
        return f"{converted_num:.2f}"

    elif (base_temp == "Kelvin") and (target_temp == "Celsius"):
        converted_num = num - 273
        return f"{converted_num:.2f}"

    elif (base_temp == "Kelvin") and (target_temp == "Kelvin"):
        converted_num = num
        return f"{converted_num:.2f}"