'''
Latency Througput Information Extractor from WRK-2 througput measurement tool
Author: Pavan Kumar Paluri
Copyright @ RTLAB - UH
'''
import re
import csv
import os.path

csv_file_result = "rtds_one_mb.csv"

# PATHS
base_path = '/root/torch/wrk2/results/one_mb/'
file_format = 'txt'


def get_time_unit(time_str):
    x = re.search(r"^(\d+\.*\d*)(\w*)$", time_str)
    if x is not None:
        prefix = float(x.group(1))
        suffix = (x.group(2)).lower()
        # print(f"prefix: {prefix} and suffix: {suffix}")
    else:
        return time_str

    # Suffix comparisons: return all the measurements in (ms) only.
    if suffix == 'us':  # micro seconds
        return prefix / 1000
    elif suffix == 'ms':  # milli seconds
        return prefix
    elif suffix == 's':  # seconds
        return prefix * 1000
    elif suffix == 'm':  # minutes
        return prefix * 1000 * 60
    elif suffix == 'h':  # hours
        return prefix * 1000 * 60 * 60
    else:  # If nothing specified, treat it as ms
        return prefix


def parse_wrk2_output(wrk_output, r_1, r_2, r_3, r_4):
    retval = {}

    for line in wrk_output.splitlines():
        # Declare Reg-ex as a raw-string
        # Step-1: Latency Match
        x = re.search(r"^\s+Latency\s+(\d+\.\d+\w*)\s+(\d+\.\d+\w*)\s+(\d+\.\d+\w*).*$", line)
        if x is not None:
            # Assign a key-val pair to each of max/mean latencies
            retval['lat_mean'] = get_time_unit(x.group(1))
            retval['lat_max'] = get_time_unit(x.group(3))

        # step-2: Throughput Match
        x = re.search(r"^\s+Req/Sec\s+(\d+\.\d+\w*)\s+(\d+\.\d+\w*)\s+(\d+\.\d+\w*).*$", line)
        if x is not None:
            retval['thrpt_avg'] = get_time_unit(x.group(1))
            retval['thrpt_max'] = get_time_unit(x.group(3))

        # step-3: 99%ile Match - Average of all 99%ile Values
        x = re.search(r"99.000%\s+(\d+\.\d+\w*).*$", line)
        if x is not None:
            r_1 = get_time_unit(x.group(1))
        x = re.search(r"99.900%\s+(\d+\.\d+\w*).*$", line)
        if x is not None:
            r_2 = get_time_unit(x.group(1))
        x = re.search(r"99.990%\s+(\d+\.\d+\w*).*$", line)
        if x is not None:
            r_3 = get_time_unit(x.group(1))
        x = re.search(r"99.999%\s+(\d+\.\d+\w*).*$", line)
        if x is not None:
            r_4 = get_time_unit(x.group(1))

        # cal average of all and store it in dict retval
        avg_99_ile = (r_1 + r_2 + r_3 + r_4) / 4
        retval['99%ile'] = round(avg_99_ile, 2)
    print(retval)
    return retval


def csv_ready(wrk_dictionary: dict):
    with open(csv_file_result, 'a', newline="") as csv_file:
        is_file_empty = os.stat(csv_file_result).st_size == 0
        headers = ['99%ile', 'lat_mean', 'lat_max', 'thrpt_avg', 'thrpt_max']
        writer = csv.DictWriter(csv_file, delimiter=',', lineterminator='\n',
                                fieldnames=headers)
        if is_file_empty:
            writer.writeheader()  # If no such file exists already, then write header

        values_list = [None] * 5  # As we know the length of this list to be 5
        counter = 0

        for key, value in wrk_dictionary.items():
            # values_list.append(value)
            if key in headers:
                # Get the index of headers[key]
                get_index = headers.index(key)
                # Use this index to load values_list
                values_list[get_index] = value

        print(values_list)
        # Finally Load it into the csv file
        writer.writerow({headers[0]: values_list[0], headers[1]: values_list[1],
                         headers[2]: values_list[2], headers[3]: values_list[3],
                         headers[4]: values_list[4]})


if __name__ == '__main__':
    file_inp = input("Please Enter the WRK Output file:")
    with open(os.path.join(base_path, file_inp), 'r') as wrk_file:
        list_txt = wrk_file.read()
    print(str(list_txt))
    reading_1, reading_2, reading_3, reading_4 = 0, 0, 0, 0
    wrk_dict = parse_wrk2_output(str(list_txt), reading_1, reading_2, reading_3, reading_4)
    csv_ready(wrk_dict)
