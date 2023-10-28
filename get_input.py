from random import shuffle

from constants import ASTAR_ALGO, UCS_ALGO
from models import Node

"""
Pulbic Methods
"""


def get_inputs() -> list[int]:
    """
    This function will prompt user input and generate appropriate data based on user command.

    Possible values:
        (1) Manually input all values of pancakes
        (2) Auto generate unordered list of values with specify max value

    Notes:
        For manual, if the input is not a valid number, it will continuously ask the user to re-input until success
    """
    input_choice = _get_pancake_choice()
    unordered_pancakes_stack = []

    match (input_choice):
        case 1:
            unordered_pancakes_stack = _get_user_input_pancake_values()
        case 2:
            num_of_digits_to_generate = input("What is the max value of the pancakes? ")

            while (
                not num_of_digits_to_generate.isdigit()
                or int(num_of_digits_to_generate) < 3
            ):
                num_of_digits_to_generate = input(
                    "Invalid input! Choice should be greater than 2 and is a number: "
                )
            unordered_pancakes_stack = list(
                range(1, int(num_of_digits_to_generate) + 1, 1)
            )
            shuffle(unordered_pancakes_stack)

    _get_algo_choice()
    return unordered_pancakes_stack


"""
Private Methods
"""


def _get_algo_choice():
    param_options = (
        "Pick the algorithm to use: \n"
        + "(1): A* search\n"
        + "(2): Uniform-cost search\n"
        + "Your choice: "
    )

    is_valid_command, input_choice = False, 0
    while not is_valid_command:
        command = input(param_options)
        is_valid_command = _is_valid_choice_of_1_or_2(command)
        input_choice = int(command)

    match (input_choice):
        case 1:
            type = ASTAR_ALGO
        case 2:
            type = UCS_ALGO
        case default:
            type = UCS_ALGO

    Node.type = type


def _is_valid_choice_of_1_or_2(command: str) -> bool:
    return command.isdigit() and int(command) > 0 and int(command) < 3


def _is_list_has_non_digit_str(str_list: list[str]) -> bool:
    return any(list(map(lambda s: not s.isdigit(), str_list)))


def _is_valid_list(str_list: list[str]) -> bool:
    seen = set()
    sorted_list = sorted(str_list)
    for idx in range(len(sorted_list)):
        val_int = int(sorted_list[idx])
        if val_int in seen:
            return False

        if val_int < 1 or val_int > 10:
            return False

        if idx == 0:
            continue

        if val_int - int(sorted_list[idx - 1]) > 1:
            return False

        seen.add(val_int)

    return True


def _get_pancake_choice() -> int:
    param_options = (
        "Pick an option: \n"
        + "(1): Input the pancakes unique values yourself\n"
        + "(2): Auto generate unordered list of pancake values\n"
        + "Your choice: "
    )

    is_valid_command, input_choice = False, 0
    while not is_valid_command:
        command = input(param_options)
        is_valid_command = _is_valid_choice_of_1_or_2(command)
        input_choice = int(command)

    return input_choice


def _is_input_list_valid(input: list[str]):
    does_list_has_non_digit = _is_list_has_non_digit_str(input)
    is_valid_for_testing = _is_valid_list(input)
    return not does_list_has_non_digit and is_valid_for_testing


def _get_user_input_pancake_values() -> list[int]:
    values = input("Enter the numbers, separated by spaces: ")
    splitted_vals = values.strip().split()
    is_user_input_valid = _is_input_list_valid(splitted_vals)

    while not is_user_input_valid:
        values = input(
            "Invalid value! Enter continuous unique numbers, separated by spaces: "
        )
        splitted_vals = values.strip().split()
        is_user_input_valid = _is_input_list_valid(splitted_vals)

    return list(map(int, splitted_vals))
