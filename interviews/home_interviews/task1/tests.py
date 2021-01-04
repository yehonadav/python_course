import os
from .solution import log_scanner
from .solution import get_log_files
from .solution import get_valid_log_strings
from .create_report import create_log_scan_report


strings = ['Error', 'Fatal', '', '   ']
folder_name = 'logs'


def test_get_log_files():
    log_files = get_log_files(folder_name)

    assert log_files == ['A.log', 'B.log', 'C.log']


def test_get_valid_log_strings():
    valid_strings = get_valid_log_strings(strings)

    assert len(valid_strings) == 2
    assert strings[0] in valid_strings
    assert strings[1] in valid_strings


def test_log_scanner():
    results = log_scanner(strings, folder_name)

    print('')
    for i in results:
        print(i)

    assert len(results) == 3
    assert results[0]['file_name'] == 'A.log' and results[0]['string'] == 'Fatal' and results[0]['count'] == 3
    assert results[1]['file_name'] == 'A.log' and results[1]['string'] == 'Error' and results[1]['count'] == 2
    assert results[2]['file_name'] == 'B.log' and results[2]['string'] == 'Error' and results[2]['count'] == 1


def test_create_log_scan_report():
    search_logs = strings
    logs_folder = folder_name
    report_filename = 'logs_report.html'

    # TODO: use report to assert test
    report = create_log_scan_report(search_logs, logs_folder, report_filename)

    try:
        with open(report_filename) as f:
            data = f.read()
            print('')
            for line in data.splitlines():
                print(line)
    finally:
        # cleanup (run in debug and stop here if you want to see the report before deletion)
        if os.path.exists(report_filename):
            os.remove(report_filename)

    # already tested in test_log_scanner
    # assert len(report) == 3
    # assert report[0]['file_name'] == 'A.log' and report[0]['string'] == 'Fatal' and report[0]['count'] == 3
    # assert report[1]['file_name'] == 'A.log' and report[1]['string'] == 'Error' and report[1]['count'] == 2
    # assert report[2]['file_name'] == 'B.log' and report[2]['string'] == 'Error' and report[2]['count'] == 1
    # TODO: (anyone is welcome to open an issue with the solution to my TODO)
    #  test the link, and maybe test the html too =)
