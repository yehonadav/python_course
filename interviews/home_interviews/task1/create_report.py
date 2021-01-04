import os
from typing import List
from .solution import log_scanner


def create_log_scan_report(search_logs: List[str], logs_folder: str, report_filename: str):
    results = log_scanner(search_logs, logs_folder)

    # The table should be sorted by Count column (order was not specified, we chose descending)
    results.sort(key=lambda i: i['count'], reverse=True)

    html = ["""
    <html>
        <table border="1">
            <tr>
                <th>File Name</th>
                <th>String</th>
                <th>Count</th>
            </tr>
    """]

    for i in results:
        # Prefer html report while the file name is link to the file
        # (link will not work with modern browsers! nothing we can do about it)
        i['link'] = f'file:///{os.getcwd()}{os.sep}{logs_folder}{os.sep}{i["file_name"]}'

        link = i['link']
        filename = i['file_name']
        string = i["string"]
        count = i["count"]

        html.append((
            "<tr>"
                "<td>"
                    f"<a href=\"{link}\">"
                        f"{filename}"
                     "</a>"
                "</td>"
                
                "<td>"
                    f"{string}"
                "</td>"
                
                "<td>"
                    f"{count}"
                "</td>"
            "</tr>"
        ))

    html.append("</table></html>")

    with open(report_filename, 'w') as f:
        f.write('\n'.join(html))

    return results
