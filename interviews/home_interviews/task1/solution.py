from typing import List, Set
import os


def get_log_files(folder_name: str) -> List[str]:
    # - note: we don't look for nested .log files
    files = os.listdir(folder_name)
    return [file for file in files if file.endswith('.log')]


def get_valid_log_strings(strings: List[str]) -> Set[str]:
    # - note: we want to remove empty strings first
    strings = [string for string in strings if string.strip()]

    # - note: we want to remove duplicate strings first
    strings = set(strings)

    return strings


def count_string_in_files(path: str, string: str):
    with open(path) as f:
        data = f.read()
        # - note: if let's say search_string = 'Error'
        # and we have 'ErrorError' inside data,
        # the count should be 2, because the exercise
        # did not specify a word type of search,
        # for that, we would use a regex
        return data.count(string)


def log_scanner(strings: List[str], folder_name: str):
    log_file_names = get_log_files(folder_name)

    search_strings = get_valid_log_strings(strings)

    results = [
        # { file_name, string, count }
    ]

    for search_string in search_strings:
        for log_file_name in log_file_names:
            count = count_string_in_files(folder_name + os.sep + log_file_name, search_string)
            # - note: the table in the example does not contain count of 0
            if count:
                results.append({
                    "file_name": log_file_name,
                    "string": search_string,
                    "count": count,
                })

    return results
