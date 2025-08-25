import ast
from typing import List, Any


# Eg: List : [3,4,6,7,8,9,10]  k=3
# Left Shift : [7,8,9,10,3,4,6]
# Right shift : [8,9,10,3,4,6,7]

def left_shift(input_list: List[Any], k: int) -> List[Any]:

    input_list_length = len(input_list)
    k = k % input_list_length

    left_rotate_list =  input_list[k:]+ input_list[:k]
    # Alternate:
    # result = input_list[k:]
    # result = result.extend(input_list[:k])

    return left_rotate_list

def right_shift(input_list: List[Any], k: int) -> List[Any]:

    input_list_length = len(input_list)
    k = k % input_list_length

    right_rotate_list =  input_list[-k:] + input_list[:-k]

    return right_rotate_list


def main():

    user_input_list = input("Enter the list elements :")

    input_list = ast.literal_eval(user_input_list)

    user_input_k = input("Enter the k number :")

    input_k = ast.literal_eval(user_input_k)

    left_rotate = left_shift(input_list, input_k)

    right_rotate = right_shift(input_list, input_k)

    print(f'Left rotate of the {input_list} by {input_k} positions is {left_rotate}')

    print(f'Right rotate of the {input_list} by {input_k} positions is {right_rotate}')

if __name__ == '__main__':
    main()
    

