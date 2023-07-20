#!/usr/bin/python3


""" Log parsing """


import sys


def print_statistics(file_size, status_code):
    """
    print_statistics prints file size and https ststus
    Args: file_size, status_code
    Return: Nothing. Printed output
    """
    print("File size: {}".format(file_size))
    sorted_code = sorted(status_code.keys())
    for code in sorted_code:
        if status_code[code] > 0:
            print("{}: {}".format(code, status_code[code]))


codes_count = {'200': 0,
               '301': 0,
               '400': 0, '401': 0, '403': 0, '404': 0, '405': 0,
               '500': 0}

total_file_size = 0
count = 0

if __name__ == "__main__":
    try:
        for line in sys.stdin:
            try:
                status_code = line.split()[-2]
                if status_code in codes_count.keys():
                    codes_count[status_code] += 1
                file_size = int(line.split()[-1])
                total_file_size += file_size
            except Exception:
                pass
            count += 1
            if count == 10:
                print_statistics(total_file_size, codes_count)
                count = 0
    except KeyboardInterrupt:
        print_statistics(total_file_size, codes_count)
        raise
    print_statistics(total_file_size, codes_count)
