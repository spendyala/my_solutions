#!/usr/bin/env python3

import csv
# import datetime

from datetime import datetime, timedelta

PAST_DAYS = 7

def main():
    fieldnames = ['User', 'Name', 'Date', 'changes']
    # end_date = datetime.datetime.now()
    # end_date = datetime.datetime(2005, 4, 20)
    # start_date = end_date - datetime.timedelta(days=PAST_DAYS)
    end_date = datetime(2005, 4, 20)
    start_date = end_date - timedelta(days=PAST_DAYS)
    total_count = 0
    range_records_count = 0
    with open('output.csv', 'w') as output_file:
        output_file_csv = csv.DictWriter(output_file, fieldnames=fieldnames)
        output_file_csv.writeheader()
        with open('smallwikipedia.csv', 'r') as smallwikipedia:
            csv_object = csv.DictReader(smallwikipedia, delimiter=';')
            for each in csv_object:
                try:
    #                 print(each)
    #                 print(each.get('Date'))
                    total_count += 1
                    # date_obj = datetime.datetime.strptime(
                    date_obj = datetime.strptime(
                        each.get('Date'), '%d/%m/%Y %H:%M')
                    if start_date < date_obj < end_date:
                        range_records_count += 1
                        output_file_csv.writerow(each)
                except Exception:
                    continue
    print(f'Total count: {total_count}')
    print(f'Range count: {range_records_count}')

if __name__ == '__main__':
    main()
