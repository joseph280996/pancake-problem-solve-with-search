from get_input import get_inputs
from models import SortingSearch, Node


if __name__ == "__main__":
    pancakes = get_inputs()

    if pancakes == sorted(pancakes):
        print("Nothing to sort here.")
    else:
        print("Start searching with input: " + str(pancakes))

        search = SortingSearch(pancakes)
        search.find_solution()

        if search.has_solution():
            search.print_solution()
