def expressions(numbers, current_result):
    if not numbers:
        return [current_result]
    result_plus = expressions(numbers[1:], current_result + numbers[0])
    result_minus = expressions(numbers[1:], current_result - numbers[0])
    return result_plus + result_minus


result = expressions([1] * 3, 0)
print(result)