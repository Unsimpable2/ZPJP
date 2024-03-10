
########## ZAD 2a
names = ["Witek", "Natalia", "Lukasz", "Jola", "Grzegorz"]

def print_names(names):
    for xd in names:
        print(xd)

print_names(names)

########## ZAD 2b

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

########## ZAD 2c

range_go_brrr = list(range(0, 10))

def even_numbers(range_go_brrr):
    for xd in range_go_brrr:
        if xd % 2 == 0:
            print(xd)

even_numbers(range_go_brrr)

########## ZAD 2d

range_go_even_more_brrr = list(range(10, 19))

def just_second_element(range_go_even_more_brrr):
    print(range_go_even_more_brrr[::2])

just_second_element(range_go_even_more_brrr)