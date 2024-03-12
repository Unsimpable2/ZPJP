numbers = [1, 2, 3, 4, 5]
output_list_v1 = []


def number_operations_v1(numbers):
    for xd in numbers:
        output_list_v1.append(xd * 2)
    return output_list_v1


print(number_operations_v1(numbers))


def number_operations_v2(numbers):
    output_list_v2 = [2 * xd for xd in numbers]
    return output_list_v2


print(number_operations_v2(numbers))
