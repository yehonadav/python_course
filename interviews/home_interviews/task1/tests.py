def test_get_log_files():
    from .solution import get_log_files

    log_files = get_log_files('logs')

    assert log_files == ['A.log', 'B.log', 'C.log']


def test_get_valid_log_strings():
    from .solution import get_valid_log_strings

    strings = ['Error', 'Fatal', '', '   ']
    valid_strings = get_valid_log_strings(strings)

    assert len(valid_strings) == 2
    assert strings[0] in valid_strings
    assert strings[1] in valid_strings


def test_log_scanner():
    from .solution import log_scanner

    strings = ['Error', 'Fatal', '', '   ']
    folder_name = 'logs'

    results = log_scanner(strings, folder_name)

    print(results)


def test_create_log_scan_report():
    from .create_report import create_log_scan_report
    import os

    search_logs = ['Error', 'Fatal', '', '   ']
    logs_folder = 'logs'
    report_filename = 'logs_report.html'

    report = create_log_scan_report(search_logs, logs_folder, report_filename)

    print('')
    for i in report:
        print(i)

    try:
        with open(report_filename) as f:
            data = f.read()
            print('')
            for line in data.splitlines():
                print(line)
    finally:
        # cleanup
        if os.path.exists(report_filename):
            os.remove(report_filename)

    assert len(report) == 3
    assert report[0]['file_name'] == 'A.log' and report[0]['string'] == 'Fatal' and report[0]['count'] == 3
    assert report[1]['file_name'] == 'A.log' and report[1]['string'] == 'Error' and report[1]['count'] == 2
    assert report[2]['file_name'] == 'B.log' and report[2]['string'] == 'Error' and report[2]['count'] == 1
