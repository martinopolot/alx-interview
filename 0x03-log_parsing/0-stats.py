#!/usr/bin/python3
"""
a script that reads stdin line by line and computes metrics
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
(if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C), 
print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size> (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code t appear or is not an integer, t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending orde
"""

from sys import stdin

if __name__ == "__main__":
    total_size = 0
    status_codes = {}
    list_status_codes = [
        "200", "301", "400", "401", "403", "404", "405", "500"]
    for status in list_status_codes:
        status_codes[status] = 0
    count = 0
    try:
        for line in stdin:
            try:
                args = line.split(" ")
                if len(args) != 9:
                    pass
                if args[-2] in list_status_codes:
                    status_codes[args[-2]] += 1
                if args[-1][-1] == '\n':
                    args[-1][:-1]
                total_size += int(args[-1])
            except:
                pass
            count += 1
            if count % 10 == 0:
                print("File size: {}".format(total_size))
                for status in sorted(status_codes.keys()):
                    if status_codes[status] != 0:
                        print("{}: {}".format(
                            status, status_codes[status]))
        print("File size: {}".format(total_size))
        for status in sorted(status_codes.keys()):
            if status_codes[status] != 0:
                print("{}: {}".format(status, status_codes[status]))
    except KeyboardInterrupt as err:
        print("File size: {}".format(total_size))
        for status in sorted(status_codes.keys()):
            if status_codes[status] != 0:
                print("{}: {}".format(status, status_codes[status]))
        raise
