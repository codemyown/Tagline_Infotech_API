def consecutive_incremental_numbers(s):
    result = []
    current_num = ""
    for digit in s:
        if current_num == "":
            current_num = digit
        elif int(digit) == int(current_num[-1]) + 1:
            current_num += digit
        else:
            if len(current_num) >= 2:
                result.append(current_num)
            current_num = digit
    if len(current_num) >= 2:
        result.append(current_num)
    return result

input_str = input("Enter Value : ")
output = consecutive_incremental_numbers(input_str)
print("Input:", input_str)
print("Output:", ', '.join(output))