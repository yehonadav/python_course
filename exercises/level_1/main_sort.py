from exercises.data import get_data
from exercises.level_1.sort_data import sort_names_with_addresses
from exercises.level_1.sort_data import add_random_postal
from exercises.level_1.sort_data import sum_postal_codes


if __name__ == "__main__":
    data = get_data(30)
    result1 = sort_names_with_addresses(data)
    result2 = add_random_postal(result1)
    result3 = sum_postal_codes(result2)
    print(result1)
    print(result2)
    print(result3)
